#!/usr/bin/env python3
"""host_info — CPU / OS / container metadata for witness benchmarks.

So the wall-times in scaling witnesses are interpretable across machines,
attach the hardware + OS + container image a compute ran on. Best-effort
and graceful: every field degrades to None off-sandbox.

PRIVACY: captures NO credentials or PII — no email, account UUID, OAuth
token, or session IDs (these witnesses are committed to a public repo).
Only hardware, OS, and the container IMAGE (repo:tag) are recorded.
"""
from __future__ import annotations

import os
import platform
import re


def _cpuinfo() -> dict:
    model = mhz = logical = physical = None
    try:
        txt = open("/proc/cpuinfo").read()
        m = re.search(r"model name\s*:\s*(.+)", txt)
        model = m.group(1).strip() if m else None
        mh = re.search(r"cpu MHz\s*:\s*([\d.]+)", txt)
        mhz = float(mh.group(1)) if mh else None
        logical = len(re.findall(r"^processor\s*:", txt, re.MULTILINE))
        pairs = set(zip(re.findall(r"physical id\s*:\s*(\d+)", txt),
                        re.findall(r"core id\s*:\s*(\d+)", txt)))
        physical = len(pairs) or None
    except Exception:
        pass
    return {"model": model, "mhz": mhz,
            "logical_cores": logical or os.cpu_count(),
            "physical_cores": physical}


def _os_pretty_name() -> str | None:
    try:
        for line in open("/etc/os-release"):
            if line.startswith("PRETTY_NAME="):
                return line.split("=", 1)[1].strip().strip('"')
    except Exception:
        pass
    return None


def _mem_total_kb() -> int | None:
    try:
        for line in open("/proc/meminfo"):
            if line.startswith("MemTotal:"):
                return int(line.split()[1])
    except Exception:
        pass
    return None


def _docker_image() -> str | None:
    repo = os.environ.get("ANT_IMAGE_REPOSITORY")
    tag = os.environ.get("ANT_IMAGE_TAG")
    if repo and tag:
        return f"{repo}:{tag}"
    return repo or None


def host_info() -> dict:
    """JSON-safe machine description for a witness `host` field."""
    try:
        import mpmath
        mpmath_ver = getattr(mpmath, "__version__", None)
    except Exception:
        mpmath_ver = None
    lib, ver = platform.libc_ver()
    return {
        "cpu": _cpuinfo(),
        "memory_total_kb": _mem_total_kb(),
        "os": {
            "pretty_name": _os_pretty_name(),
            "kernel": platform.release(),
            "platform": platform.platform(),
            "libc": (f"{lib} {ver}".strip() or None),
            "machine": platform.machine(),
        },
        "python": platform.python_version(),
        "mpmath": mpmath_ver,
        "container": {
            "docker_image": _docker_image(),
            "environment_type": os.environ.get("CLAUDE_CODE_REMOTE_ENVIRONMENT_TYPE"),
            "is_sandbox": os.environ.get("IS_SANDBOX") == "yes",
        },
    }


def summary_line() -> str:
    """One-line human summary for log headers."""
    h = host_info()
    c = h["cpu"]
    mem_gb = (h["memory_total_kb"] or 0) / 1048576
    return (f"{c.get('model')} ×{c.get('logical_cores')} "
            f"({c.get('physical_cores')} phys), {mem_gb:.1f} GB | "
            f"{h['os']['pretty_name']} {h['os']['kernel']} | "
            f"py{h['python']} mpmath {h['mpmath']} | img {h['container']['docker_image']}")


if __name__ == "__main__":
    import json
    print(summary_line())
    print(json.dumps(host_info(), indent=2))
