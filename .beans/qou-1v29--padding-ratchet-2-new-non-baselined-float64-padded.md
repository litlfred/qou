---
# qou-1v29
title: 'Padding ratchet: 2 NEW non-baselined float64-padded witnesses (casimir-q-zeta-probe, rho-k-h3a-lp-dual)'
status: todo
type: bug
priority: normal
created_at: 2026-09-07T09:21:12Z
updated_at: 2026-09-07T09:21:27Z
---

Found incidentally on 2026-09-07 while running `scripts/precision-gates.sh` before a
commit for bean `qou-igjo`. **Not caused by that change** — the gate run regenerated
`computations/witness-float64-padding-audit.witness.json`, which is a contended
tree-measuring audit that must not be committed from a feature branch (bean
`qou-v0t8`), so the regenerated file was reverted and only this record kept.

The audit moved:

    occurrences        22 -> 24
    distinct_values    18 -> 20
    files               7 ->  9
    live_files          2 ->  4
    new_not_baselined  10 -> 12

The two NEW non-baselined entries:

| witness | field | stored | real |
|---|---|---|---|
| `computations/probes/casimir-q-zeta-probe.witness.json` | `parameters.substrate_q` | `1.10997858275138083783417641825508326292037963867187500000000` | `1.1099785827513808` |
| `computations/rho-k-h3a-lp-dual.witness.json` | `parameters.m_n_MeV` | `939.5654217899999594010296277701854705810546875` | `939.56542179` |

Both are the textbook signature the padding audit exists for: a float64 serialized far
past ~17 digits so the binary-expansion tail reads as measured precision. `m_n_MeV`
is especially clear — the neutron mass is a CODATA input known to 9 decimals and is
stored to 46, of which 37 are an artifact of the double.

**Fix at the producer**, per the audit's own instruction: do not baseline these and do
not hand-edit the numbers. Each is a `parameters` field, so the producer is passing a
Python float into the serializer instead of an `mpf` built from the literal, or instead
of the literal string.

Distinct from `qou-5sg8` (`categorical-bypass-volmatch-demo`) and `qou-txru`
(`chi_sym_alt_closed_form`), which name different files.
