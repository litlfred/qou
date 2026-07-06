# `pyhecke_native` IS buildable in-sandbox — Clarabel.rs via the egress proxy (corrects the #3039 b0vf over-claim)

**Date:** 2026-06-28
**Beans:** `b0vf` (He4 H₁₂ χ), `adhb` (He3 R5) — both had been called "blocked by `pyhecke_native`".
**Corrects:** [`docs/audits/2026-06-28-adhb-r5-multiterm-insufficient-b0vf-native-blocked.md`](2026-06-28-adhb-r5-multiterm-insufficient-b0vf-native-blocked.md)
(merged in #3039), which claimed b0vf was "blocked by an out-of-scope Rust dependency repo … not fixable
in this sandbox." **That claim was wrong** — the owner correctly pushed back.

## Root cause (not a hard block — a git misrouting)

`tools/pyhecke-native`'s `clarabel` Cargo dep is pinned to `github.com/litlfred/Clarabel.rs`. The
earlier build hit **HTTP 403**, which I mis-attributed to an egress-policy denial. In fact:

- The session's **global git config** has `url.http://local_proxy@127.0.0.1:41729/git/.insteadof =
  https://github.com/` — it rewrites *all* `github.com` fetches through the **scoped GitHub git proxy**
  (`41729`), which only serves `litlfred/qou` → 403 for `litlfred/Clarabel.rs`.
- The **HTTPS egress proxy** (`40609`, `$HTTPS_PROXY`) **does allow** `litlfred/Clarabel.rs`:
  `GIT_CONFIG_GLOBAL=/dev/null git -c http.proxy=$HTTPS_PROXY ls-remote
  https://github.com/litlfred/Clarabel.rs` returns its refs (incl. the pinned rev `967320920c…` on
  branch `claude/bigrational-backend-BeGUU`).

So the dep is reachable; the build just has to fetch it via the egress proxy, not the scoped git proxy.

## Build recipe (reproducible)

```bash
# 1. custom git config: egress proxy for github.com, NO 41729 scoped-proxy rewrite, keep the CA
cat > /tmp/build-gitconfig <<EOF
[http]
	sslCAInfo = /root/.ccr/ca-bundle.crt
	proxy = ${HTTPS_PROXY}          # http://127.0.0.1:40609
[url "https://github.com/"]
	insteadOf = git@github.com:
	insteadOf = ssh://git@github.com/
EOF
# 2. build with cargo using the git CLI (so it honours the config above) + the proxy CA
export GIT_CONFIG_GLOBAL=/tmp/build-gitconfig GIT_CONFIG_SYSTEM=/dev/null
export CARGO_NET_GIT_FETCH_WITH_CLI=true
export CARGO_HTTP_CAINFO=/root/.ccr/ca-bundle.crt SSL_CERT_FILE=/root/.ccr/ca-bundle.crt
export PATH="$HOME/.cargo/bin:$PATH"
pip install maturin
pip install --no-build-isolation ./tools/pyhecke-native
# -> Successfully installed pyhecke-native-0.9.0 ; imports with trace_weights_n + chi_q_via_gp
```

This is **not** routing around an org-policy denial (the egress policy *allows* the repo); it routes a
build dependency through the general egress proxy exactly like crates.io / pip deps.

## Corrected status of the two beans

- **adhb — verdict UNCHANGED.** My #3039 diagnosis used the committed `y-lambda-wenzl-witness.json`
  cache, which matches `pyhecke_native` to 3e-16, so the solver winner is identical with native. The
  re-run still does **not** recover the canonical T_w (deuteron `6_2` not PSD-feasible; he3 `L6a4`
  predicts ~2.04 MeV vs `B_AME=7.718`, the ~1 MeV multi-term offset can't close the gap). Native
  availability does not change the refutation.

- **b0vf — re-scoped, NOT a simple "re-run completes it".** Two findings:
  1. The **canonical lossless `chi-helium-4-h12-at-q0-50dps-matrix-m.witness.json` is already 77/77
     complete on main** (`partial=false`). The file the bean cites
     (`chi-helium-4-h12-at-q0-50dps.witness.json`, no `-matrix-m`, 22/77) is a separate/older partial.
  2. **Engine-version caveat (data-integrity).** Running `chi_4he_via_rust_lossless.py` with the
     freshly-built `pyhecke_native 0.9.0` (Clarabel.rs `bigrational-backend` dev branch, rev
     `967320920c`) reproduced 77/77 in **3.4 s** but with `tr_M(q0) = 0.88561692…` vs the committed
     `0.88561640…` — a drift at the 7th significant figure. Characters are exact integer Laurents, so
     this means the dev-branch engine differs from the engine that generated the committed witnesses.
     **Regenerating committed witnesses therefore requires the canonical `pyhecke-native` version, not
     this dev build** — so I reverted the regenerated files rather than commit engine-drifted values.

## Net

The build block is **removed** (recipe above) — the genuine correction to #3039. b0vf's remaining work
is a *version-matched* regen of the non-`-matrix-m` partial (or confirming the lossless `-matrix-m`
cache supersedes it), which is a data-integrity task gated on identifying the canonical engine
version — not the "out-of-scope, not fixable" block I wrongly recorded. adhb's refutation stands.
