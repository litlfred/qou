#!/usr/bin/env python3
"""Fetch a claude.ai account's conversations via its internal endpoints.

Writes a conversations.json compatible with archive_sessions.py — the
scriptable alternative to the official Settings → Privacy → Export data
flow and the browser-console snippet.

UNOFFICIAL: uses claude.ai's internal, undocumented web endpoints. It can
break whenever Anthropic changes them, and automated access may be against
the consumer Terms of Service — it is your own data, but you accept that
risk. Cloudflare sometimes blocks non-browser clients; if you get HTTP 403
with a challenge page, use browser-export-snippet.js instead.

Authentication — the sessionKey cookie (NEVER paste it into a chat, commit,
or share it; it grants full access to your Claude account):

    1. Log in to claude.ai in a browser.
    2. DevTools → Application/Storage → Cookies → https://claude.ai →
       copy the value of the `sessionKey` cookie (starts with "sk-ant-sid01-").
    3. Export it and run (do NOT pass it on the command line — it would
       land in your shell history / process list):

         export CLAUDE_SESSION_KEY='sk-ant-sid01-...'
         python3 human-agent-discussions/tools/fetch_claude_export.py \
             --out human-agent-discussions/_incoming/<account>/conversations.json

Then archive as usual:

    python3 human-agent-discussions/tools/archive_sessions.py

Stdlib only.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request

BASE = "https://claude.ai"
UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")


def log(msg):
    print(msg, file=sys.stderr)


def api_get(path, session_key, timeout=30):
    req = urllib.request.Request(
        BASE + path,
        headers={
            "Cookie": "sessionKey=" + session_key,
            "User-Agent": UA,
            "Accept": "application/json",
            "Referer": BASE + "/",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace")[:200]
        if e.code in (401, 403):
            raise SystemExit(
                "HTTP %d from %s — session key invalid/expired, or Cloudflare "
                "blocked the request.\nGet a fresh sessionKey, or use "
                "browser-export-snippet.js.\nResponse head: %s"
                % (e.code, path, body))
        raise SystemExit("HTTP %d from %s: %s" % (e.code, path, body))
    except (urllib.error.URLError, TimeoutError) as e:
        raise SystemExit("network error on %s: %s" % (path, e))


def pick_org(session_key, want=None):
    orgs = api_get("/api/organizations", session_key)
    if not isinstance(orgs, list) or not orgs:
        raise SystemExit("no organizations returned — is the session key valid?")
    if want:
        for o in orgs:
            if o.get("uuid") == want or o.get("name") == want:
                return o
        raise SystemExit("org %r not found; available: %s"
                         % (want, ", ".join(o.get("name", o.get("uuid", "?")) for o in orgs)))
    for o in orgs:
        if "chat" in (o.get("capabilities") or []):
            return o
    return orgs[0]


def list_conversations(org_uuid, session_key, since=None):
    out, offset = [], 0
    while True:
        page = api_get(
            "/api/organizations/%s/chat_conversations?limit=100&offset=%d"
            % (org_uuid, offset), session_key)
        if isinstance(page, dict):
            page = page.get("conversations") or page.get("data") or []
        if not page:
            break
        known = {c.get("uuid") for c in out}
        fresh = [c for c in page if c.get("uuid") not in known]
        out.extend(fresh)
        if len(page) < 100 or not fresh:
            break
        offset += len(page)
        time.sleep(0.2)
    if since:
        out = [c for c in out
               if (c.get("updated_at") or c.get("created_at") or "") >= since]
    return out


def fetch_full(org_uuid, conv_uuid, session_key):
    return api_get(
        "/api/organizations/%s/chat_conversations/%s"
        "?tree=True&rendering_mode=messages&render_all_tools=true"
        % (org_uuid, conv_uuid), session_key)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", required=True, help="output conversations.json path")
    ap.add_argument("--org", help="organization uuid or name (default: first chat org)")
    ap.add_argument("--since", help="skip conversations last updated before YYYY-MM-DD")
    ap.add_argument("--delay", type=float, default=0.3,
                    help="seconds between conversation fetches (default 0.3)")
    ap.add_argument("--limit", type=int, default=0,
                    help="fetch at most N conversations (0 = all)")
    args = ap.parse_args(argv)

    session_key = os.environ.get("CLAUDE_SESSION_KEY", "").strip()
    if not session_key:
        raise SystemExit(
            "Set CLAUDE_SESSION_KEY in the environment (NOT on the command "
            "line). See this file's header for how to obtain it.")
    if not session_key.startswith("sk-ant-sid"):
        log("WARN: session key does not look like 'sk-ant-sid...'; continuing anyway")

    org = pick_org(session_key, args.org)
    org_uuid = org["uuid"]
    log("org: %s (%s)" % (org.get("name", "?"), org_uuid))

    convs = list_conversations(org_uuid, session_key, args.since)
    if args.limit:
        convs = convs[:args.limit]
    log("%d conversation(s) to fetch" % len(convs))

    out, failed = [], 0
    for i, c in enumerate(convs, 1):
        cu = c.get("uuid")
        try:
            full = fetch_full(org_uuid, cu, session_key)
            out.append(full)
            log("  %d/%d  %s" % (i, len(convs), full.get("name") or cu))
        except SystemExit:
            raise
        except Exception as e:  # noqa: BLE001 — keep going on a single bad conv
            failed += 1
            log("  %d/%d  FAILED %s: %s" % (i, len(convs), cu, e))
        time.sleep(args.delay)

    out_path = os.path.abspath(os.path.expanduser(args.out))
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False)
    log("wrote %d conversation(s) to %s%s"
        % (len(out), out_path, " (%d failed)" % failed if failed else ""))
    log("next: python3 human-agent-discussions/tools/archive_sessions.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
