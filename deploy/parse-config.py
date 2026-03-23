#!/usr/bin/env python3
"""Parse lean-mcp.config.json and emit deploy config as KEY=VALUE to $GITHUB_OUTPUT."""

import json
import os
import sys

config_path = sys.argv[1] if len(sys.argv) > 1 else "lean-mcp.config.json"
c = json.load(open(config_path))
f = c.get("folio", {})
h = c.get("hetzner", {})
a = c.get("auth", {})

output_file = os.environ.get("GITHUB_OUTPUT")
if not output_file:
    print("Error: GITHUB_OUTPUT not set", file=sys.stderr)
    sys.exit(1)

with open(output_file, "a") as out:
    out.write(f"domain={f.get('domain', 'folio.example.org')}\n")
    out.write(f"image={c.get('image', 'ghcr.io/litlfred/qou/paper-assistant')}\n")
    out.write(f"mcp_port={c.get('mcp_internal_port', 8080)}\n")
    out.write(f"viewer_dir={f.get('viewer_dir', 'viewer')}\n")
    out.write(f"owner_username={a.get('owner', 'litlfred')}\n")
    out.write(f"session_max_age={a.get('session_max_age_hours', 24) * 3600}\n")
    out.write(f"server_type={h.get('server_type', 'cx22')}\n")
    out.write(f"location={h.get('location', 'fsn1')}\n")
    out.write(f"server_image={h.get('image', 'ubuntu-24.04')}\n")
