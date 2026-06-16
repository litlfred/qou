# Coordination — 2 mass-table scripts broken on main (finding)

**Date:** 2026-05-24
**Status:** NEGATIVE FINDING — Pre-existing bugs surfaced during the
mass-table staleness sweep; not introduced by any session work.
**Trigger:** Mass-table staleness sweep (PR #1065 era) showed 7 of 8
mass-table witnesses stale. After PR #1077 deleted the 3 truly-orphan
witnesses (m3 / m4 / m5; producer scripts gone), 2 remain stale with
producer scripts alive: `applied_uniqueness_mass_table.py` and
`isotope-mass-table.py`. Attempting to re-run them surfaced **two
distinct pre-existing bugs**.

## Bug 1 — `applied_uniqueness_mass_table.py`: missing-import cascade

```
ModuleNotFoundError: No module named 'derive_m_p_hecke_path_a'
  imported by derivation_chain.py:208
  consumed by applied_uniqueness_mass_table.py via categorical_mass_via_ratio
```

`derive_m_p_hecke_path_a.py` was **moved** (not deleted) by
commit [`aac4f0050`](https://github.com/litlfred/qou/commit/aac4f0050)
("cleanup(batch2): move 148 probes + 2 deprecated to `_deprecated/`")
to `_deprecated/superseded/derive_m_p_hecke_path_a.py` — but the
4 importers on the main path were not updated:

- `computations/derivation_chain.py:208`
- `computations/derive_m_p_hecke_full_tower_50dps.py`
- `computations/derive_m_n_hecke_path_a.py`
- `computations/derive_m_e_hecke_path_a.py`

All 4 are silently broken on `main` until someone invokes them.

### Fix paths (any one of)

1. **Restore** `derive_m_p_hecke_path_a.py` to the canonical path
   (un-deprecate). Lowest risk; preserves the existing API.
2. **Update importers** to use the canonical replacement. Requires
   identifying what supersedes `m_p_hecke_path_a_at_q0` — likely
   one of the newer `derive_m_p_*_50dps.py` scripts, but a careful
   audit is needed.
3. **Patch the import** in `derivation_chain.py` to fall back to
   the `_deprecated/superseded/` location via `importlib`. Hack;
   not recommended.

## Bug 2 — `isotope-mass-table.py`: `mpf.__format__` regression

```
TypeError: unsupported format string passed to mpf.__format__
  at isotope-mass-table.py:288 in main()
  format string: f"{iso_name:<8} {Z:>3} {N:>3} {A:>3} ..."
```

Likely the format string contains a `mpmath.mpf` value (e.g. `B/A`
column) that doesn't support all numeric format codes (`%f`, `:.6f`
etc. work; some don't). Either:

- A recent mpmath version regression (mpmath 1.3.0 currently
  installed)
- A pre-existing bug that no one notices because the script isn't
  in CI

The fix is local: wrap `mpf` values in `float(...)` or `mp.nstr(...)`
before passing to the format string.

## What this doc does NOT do

- **Does not restore** `derive_m_p_hecke_path_a.py` — the right
  fix path needs author input on whether the script is genuinely
  superseded.
- **Does not fix** the `mpf.__format__` regression — needs a small
  audit of which column triggered it.
- **Does not re-run** either mass table — both blocked on the
  fixes above.

## What this doc DOES

Records the findings so the next session / agent can pick them up
without re-discovery. Both bugs were surfaced by the post-deprecation
witness staleness sweep; PR #1077 cleaned up the orphan witnesses
that should not be regenerated, leaving these 2 alive-but-broken
scripts as the genuine technical-debt items.

## Mass-table staleness state after PR #1077

| witness | state | next |
|---|---|---|
| `canonical-mass-table-extended` | re-running in #1064 (merged) | — |
| `applied-uniqueness-mass-table` | stale | **Bug 1 fix → re-run** |
| `isotope-mass-table` | stale | **Bug 2 fix → re-run** |
| `mass-table-ppb` | fresh | — |
| `low-isotope-mass-table` | wrapper in #1065 | merge #1065 |
| `m3` / `m4` / `m5` mass-table | deleted in #1077 | — |

## Related

- [PR #1077](https://github.com/litlfred/qou/pull/1077) — orphan witness deletion
- [PR #1065](https://github.com/litlfred/qou/pull/1065) — low-isotope wrapper
- [`aac4f0050`](https://github.com/litlfred/qou/commit/aac4f0050) — the cleanup commit that left the import cascade broken
