# Google OAuth Setup for QOU Folio

The **only manual secrets** required for the folio deployment are a Google
OAuth Client ID and Client Secret. Everything else is auto-generated or
read from `lean-mcp.config.json` (version-controlled, no secrets).

## Recommended: GitHub Secrets (no SSH required)

This is the zero-SSH approach. You never touch the server directly.

### 1. Create Google OAuth credentials (~3 min)

1. Go to https://console.cloud.google.com/projectcreate — name it "QOU Folio"
   (no billing required)
2. **APIs & Services > OAuth consent screen** → External → fill in app name +
   emails → **Publish App**
3. **APIs & Services > Credentials** → **+ Create Credentials > OAuth client ID**
   - Type: **Web application**
   - Redirect URI: `https://folio.litlfred.org/oauth2/callback`
4. Copy the **Client ID** and **Client Secret**

### 2. Add GitHub repo secrets (~1 min)

Go to **Settings > Secrets and variables > Actions** in your GitHub repo.
Add these three repository secrets:

| Secret name | Value | Where to get it |
|-------------|-------|-----------------|
| `HETZNER_API_TOKEN` | Hetzner Cloud API token | https://console.hetzner.cloud/ → project → API tokens |
| `GOOGLE_CLIENT_ID` | `123...apps.googleusercontent.com` | Step 1 above |
| `GOOGLE_CLIENT_SECRET` | `GOCSPX-...` | Step 1 above |

### 3. Run the deploy workflow (~5 min)

1. Go to **Actions > Deploy Folio** in your GitHub repo
2. Click **Run workflow** → action: **provision**
3. Wait for it to complete — it prints the server IP
4. Point DNS: `folio.litlfred.org` → A record → that IP

Done. Caddy auto-provisions TLS. Self-updater handles all future updates.

### Updating secrets

If you rotate Google OAuth credentials:

1. Update the GitHub secrets
2. Run **Actions > Deploy Folio** → action: **update**

This uses `hcloud server ssh` (Hetzner console access) to push the new
`.env` to the server. No SSH keys, no direct server access.

### Destroying

Run **Actions > Deploy Folio** → action: **destroy**. Remove the DNS record.

---

## Alternative: manual SSH setup

If you prefer to manage secrets directly on the server:

1. Complete step 1 above (create Google OAuth credentials)
2. SSH into the server: `ssh root@<IP>`
3. Edit `/opt/qou/deploy/.env`:
   ```
   GOOGLE_CLIENT_ID=123456789-xxxxx.apps.googleusercontent.com
   GOOGLE_CLIENT_SECRET=GOCSPX-xxxxxxxxxxxxxxxxxxxxx
   ```
4. Restart: `docker compose -f docker-compose.folio.yml restart oauth2-proxy`

---

## How the auth flow works

```
User visits folio.litlfred.org
  → Caddy (TLS termination)
  → oauth2-proxy checks for session cookie
    → No cookie: redirect to Google Sign-In
    → Google authenticates user, returns email
    → oauth2-proxy checks email against authorized-emails.txt
      → Match: set session cookie, proxy to viewer / lean-mcp
      → No match: 403 Forbidden
```

## Managing the email whitelist

The whitelist is **version-controlled** in `lean-mcp.config.json`:

```json
{
  "authorized_emails": ["alice@gmail.com", "bob@example.com"]
}
```

When you commit a change to this file on `main`:
1. The self-updater (cron, every minute) detects the new commit
2. Pulls the repo
3. Regenerates `authorized-emails.txt` from the config
4. Bounces oauth2-proxy

**No SSH needed** to add/remove users — just edit the config and push.

## Security model

### What's where

| Secret | Stored in | Accessible to |
|--------|-----------|---------------|
| `GOOGLE_CLIENT_ID` | GitHub Secrets + server `.env` | Repo admins, server root |
| `GOOGLE_CLIENT_SECRET` | GitHub Secrets + server `.env` | Repo admins, server root |
| `LEAN_LSP_MCP_TOKEN` | Server `.env` only | Server root |
| `COOKIE_SECRET` | Server `.env` only | Server root |
| `HETZNER_API_TOKEN` | GitHub Secrets only | Repo admins |

### Threat model

- **GitHub Secrets** are encrypted at rest, only exposed to Actions runs.
  They appear masked in logs. Repo admins can overwrite but not read them.
- **Cloud-init** runs once at server creation. The script (with secrets) is
  stored in Hetzner's metadata — accessible only via the Hetzner API with
  your token. It's not persisted on disk after execution.
- **`.env` on server** is only readable by root. Never committed to git.
  The self-update script preserves it across `git clean`.
- **Client ID** is semi-public (visible in browser redirects). Not sensitive.
- **Client Secret** is the main secret to protect. Stored in GitHub Secrets
  (encrypted) and server `.env` (root-only).
- **oauth2-proxy** enforces the email whitelist server-side. Even if someone
  has the Google login URL, they get 403 unless their email is in the list.

### Rotating credentials

**Google OAuth** (via GitHub Actions — no SSH):
1. Reset secret in Google Cloud Console
2. Update `GOOGLE_CLIENT_SECRET` in GitHub repo secrets
3. Run Deploy Folio → action: update

**Session cookie** (logs out all users):
Run Deploy Folio → action: update (generates a new cookie secret)
