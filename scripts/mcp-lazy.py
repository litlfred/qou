#!/usr/bin/env python3
"""Lazy MCP stub: start an MCP server's backend only when an agent asks for it.

Owner, 2026-11-20: "MCP should only start up if an agent needs the tools. The
agent should look at the process and what it needs and then make a decision."

Why this exists. Every server in .mcp.json used to start at session start,
competing with the SessionStart hooks, and the session paid for it whether or
not the task needed any of them. Measured 2026-11-20, fresh container: all four
reported CONNECT_TIMEOUT (30 s), and run by hand two of them could never have
started at all. `paper-search-mcp` is unpinned and dies on mcp 2.x ("No module
named 'mcp.server.fastmcp'"); `alex-mcp` exits unless OPENALEX_MAILTO is set.

What it does. Usage: `mcp-lazy.py <server-name>`. The real command lives in
scripts/mcp-lazy.json. The stub answers `initialize` at once and exposes ONE
tool, `start`. That tool's description says what the server provides, when it
is worth starting, the cost, and the cheaper route that needs no MCP. Only a
call to `start` launches the backend. The stub then performs the backend's
`initialize` handshake, sends `notifications/tools/list_changed`, and from
then on lists the backend's tools and forwards every message both ways. The
agent calls RefreshMcpTools after `start` to see the new tools.

A failed start returns the backend's stderr tail as the tool result rather than
a silent dropped connection. That is where the two defects above surfaced.

Standard library only. Messages are newline-delimited JSON-RPC on stdio, the
MCP stdio framing.
"""
from __future__ import annotations

import atexit
import json
import os
import signal
import subprocess
import sys
import threading
import time
from collections import deque
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REGISTRY = ROOT / "scripts" / "mcp-lazy.json"

_out_lock = threading.Lock()


def send(msg: dict) -> None:
    line = json.dumps(msg, ensure_ascii=False)
    with _out_lock:
        sys.stdout.write(line + "\n")
        sys.stdout.flush()


def log(text: str) -> None:
    sys.stderr.write(f"[mcp-lazy] {text}\n")
    sys.stderr.flush()


class Backend:
    def __init__(self, name: str, spec: dict):
        self.name = name
        self.spec = spec
        self.proc: subprocess.Popen | None = None
        self.tools: list = []
        self.stderr_tail: deque = deque(maxlen=40)
        self._waiters: dict = {}
        self._lock = threading.Lock()
        self.ready = False

    # -- process plumbing -------------------------------------------------
    def _read_stdout(self) -> None:
        assert self.proc and self.proc.stdout
        for raw in self.proc.stdout:
            raw = raw.strip()
            if not raw:
                continue
            try:
                msg = json.loads(raw)
            except json.JSONDecodeError:
                self.stderr_tail.append(f"(non-JSON stdout) {raw[:200]}")
                continue
            mid = msg.get("id")
            if isinstance(mid, str) and mid.startswith("mcp-lazy:"):
                with self._lock:
                    ev = self._waiters.pop(mid, None)
                if ev is not None:
                    ev["msg"] = msg
                    ev["event"].set()
                continue
            send(msg)  # responses to client requests, notifications, server->client requests
        log(f"{self.name}: backend stdout closed")

    def _read_stderr(self) -> None:
        assert self.proc and self.proc.stderr
        for raw in self.proc.stderr:
            line = raw.rstrip("\n")
            self.stderr_tail.append(line)
            sys.stderr.write(line + "\n")
            sys.stderr.flush()

    def write(self, msg: dict) -> None:
        assert self.proc and self.proc.stdin
        self.proc.stdin.write(json.dumps(msg) + "\n")
        self.proc.stdin.flush()

    def request(self, method: str, params: dict, timeout: float) -> dict:
        rid = f"mcp-lazy:{method}:{time.monotonic_ns()}"
        ev = {"event": threading.Event(), "msg": None}
        with self._lock:
            self._waiters[rid] = ev
        self.write({"jsonrpc": "2.0", "id": rid, "method": method, "params": params})
        if not ev["event"].wait(timeout):
            raise TimeoutError(f"{method} got no answer within {timeout:.0f} s")
        msg = ev["msg"]
        if "error" in msg:
            raise RuntimeError(f"{method} returned error: {msg['error']}")
        return msg.get("result", {})

    # -- start ------------------------------------------------------------
    def start(self, client_init_params: dict) -> str:
        if self.ready:
            return f"{self.name} is already running ({len(self.tools)} tools)."
        missing = [v for v in self.spec.get("requires_env", []) if not os.environ.get(v)]
        if missing:
            raise RuntimeError(
                f"{self.name} needs environment variable(s) {', '.join(missing)}, which are not "
                "set in this session. The backend exits immediately without them, so it was not launched."
            )
        cmd = [self.spec["command"], *self.spec.get("args", [])]
        timeout = float(self.spec.get("start_timeout_s", 120))
        t0 = time.monotonic()
        self.proc = subprocess.Popen(
            cmd, cwd=ROOT, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
            stderr=subprocess.PIPE, text=True, bufsize=1,
        )
        threading.Thread(target=self._read_stdout, daemon=True).start()
        threading.Thread(target=self._read_stderr, daemon=True).start()
        params = dict(client_init_params or {})
        params.setdefault("protocolVersion", "2024-11-05")
        params.setdefault("capabilities", {})
        params.setdefault("clientInfo", {"name": "mcp-lazy", "version": "1"})
        try:
            self.request("initialize", params, timeout)
            self.write({"jsonrpc": "2.0", "method": "notifications/initialized"})
            self.tools = self.request("tools/list", {}, timeout).get("tools", [])
        except Exception as exc:
            rc = self.proc.poll()
            tail = "\n".join(list(self.stderr_tail)[-15:])
            self.stop()
            raise RuntimeError(
                f"{self.name} failed to start ({exc}; exit code {rc}). Backend stderr tail:\n{tail}"
            ) from None
        self.ready = True
        dt = time.monotonic() - t0
        log(f"{self.name}: started in {dt:.1f} s with {len(self.tools)} tools")
        return (
            f"{self.name} started in {dt:.1f} s with {len(self.tools)} tools. "
            "Call RefreshMcpTools to load them into this session."
        )

    def stop(self) -> None:
        if self.proc and self.proc.poll() is None:
            self.proc.terminate()
        self.ready = False


def start_tool(name: str, spec: dict) -> dict:
    desc = (
        f"Start the {name} MCP server. It is NOT running until you call this. "
        f"Provides: {spec.get('summary', '')} "
        f"Start it when {spec.get('use_when', 'the task needs these tools')} "
        f"Cheaper route without MCP: {spec.get('instead', 'none')} "
        f"Cost: {spec.get('cost', 'unknown')} "
        "After a successful start, call RefreshMcpTools to see its tools."
    )
    return {
        "name": "start",
        "description": desc,
        "inputSchema": {
            "type": "object",
            "properties": {
                "reason": {"type": "string", "description": "One line: why this task needs the server."}
            },
        },
    }


def main() -> int:
    if len(sys.argv) != 2:
        log("usage: mcp-lazy.py <server-name>")
        return 2
    name = sys.argv[1]
    servers = json.loads(REGISTRY.read_text())["servers"]
    if name not in servers:
        log(f"unknown server {name!r}; known: {', '.join(servers)}")
        return 2
    spec = servers[name]
    backend = Backend(name, spec)
    # The client may end the session with SIGTERM rather than closing stdin. Take
    # the backend down with us, or it is orphaned (measured: a bun server left
    # running after its proxy was terminated).
    atexit.register(backend.stop)
    signal.signal(signal.SIGTERM, lambda *_: sys.exit(0))
    client_init: dict = {}

    for raw in sys.stdin:
        raw = raw.strip()
        if not raw:
            continue
        try:
            msg = json.loads(raw)
        except json.JSONDecodeError:
            continue
        method = msg.get("method")
        mid = msg.get("id")

        if backend.ready:
            # Our own `start` tool stays available (idempotent); everything else goes through.
            if method == "tools/call" and msg.get("params", {}).get("name") == "start":
                send({"jsonrpc": "2.0", "id": mid, "result": {
                    "content": [{"type": "text", "text": backend.start(client_init)}]}})
                continue
            if method == "tools/list":
                send({"jsonrpc": "2.0", "id": mid,
                      "result": {"tools": [start_tool(name, spec), *backend.tools]}})
                continue
            backend.write(msg)
            continue

        if method == "initialize":
            client_init = msg.get("params", {})
            send({"jsonrpc": "2.0", "id": mid, "result": {
                "protocolVersion": client_init.get("protocolVersion", "2024-11-05"),
                "capabilities": {"tools": {"listChanged": True}},
                "serverInfo": {"name": f"{name} (lazy)", "version": "1"},
                "instructions": (
                    f"The {name} server has not been started. Read the `start` tool's description, "
                    "decide whether this task needs it, and call `start` only if it does."
                ),
            }})
        elif method == "tools/list":
            send({"jsonrpc": "2.0", "id": mid, "result": {"tools": [start_tool(name, spec)]}})
        elif method == "tools/call":
            tool = msg.get("params", {}).get("name")
            if tool != "start":
                send({"jsonrpc": "2.0", "id": mid, "result": {"isError": True, "content": [{
                    "type": "text", "text": f"{name} is not running; call `start` first."}]}})
                continue
            try:
                text = backend.start(client_init)
                send({"jsonrpc": "2.0", "id": mid, "result": {"content": [{"type": "text", "text": text}]}})
                send({"jsonrpc": "2.0", "method": "notifications/tools/list_changed"})
            except Exception as exc:
                send({"jsonrpc": "2.0", "id": mid, "result": {"isError": True, "content": [{
                    "type": "text", "text": str(exc)}]}})
        elif method in ("prompts/list",):
            send({"jsonrpc": "2.0", "id": mid, "result": {"prompts": []}})
        elif method in ("resources/list",):
            send({"jsonrpc": "2.0", "id": mid, "result": {"resources": []}})
        elif method in ("resources/templates/list",):
            send({"jsonrpc": "2.0", "id": mid, "result": {"resourceTemplates": []}})
        elif method == "ping":
            send({"jsonrpc": "2.0", "id": mid, "result": {}})
        elif mid is not None and method is not None:
            send({"jsonrpc": "2.0", "id": mid, "error": {
                "code": -32601, "message": f"{method}: {name} is not running; call the `start` tool first."}})
        # notifications before start (initialized, cancelled, ...) are dropped

    backend.stop()
    return 0


if __name__ == "__main__":
    sys.exit(main())
