---
# qou-6irj
title: 'wrap_legacy never stamps q0Anchor: 1,924 of 3,477 witnesses (55.3%) are invisible to every q0-anchor audit; 384 of them carry a q0 value'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-04T03:21:09Z
updated_at: 2026-10-04T15:25:40Z
parent: qou-5vkl
---

## Measured 2026-09-04 (branch claude/standard-model-terms-status-ftoejr)

    witnesses                        3477
      no q0Anchor key                1924  (55.3%)
      ...and carry a q0 value         384
    producers using wrap_legacy       282

Reproduce (both numbers, from the repo root):

    grep -rl "wrap_legacy" --include=*.py computations/ | wc -l
    python3 - <<'PY'
    import json, glob
    PRE = ["1.1099785827513808","1.1099785956427390","1.1099785955541805",
           "1.1099785955573347","1.109978595"]
    def carries(o):
        if isinstance(o,str):  return any(p in o for p in PRE)
        if isinstance(o,(int,float)): return str(o).startswith("1.109978")
        if isinstance(o,dict): return any(carries(v) for v in o.values())
        if isinstance(o,list): return any(carries(v) for v in o)
        return False
    tot=unst=q0=0
    for f in glob.glob("computations/**/*.witness.json", recursive=True):
        try: d=json.load(open(f))
        except Exception: continue
        if not isinstance(d,dict): continue
        tot+=1
        if "q0Anchor" not in d:
            unst+=1
            if carries(d): q0+=1
    print(tot, unst, q0)
    PY

## The mechanism

`WitnessBuilder.wrap_legacy` documents exactly what it adds: `scriptHash`,
`scriptCommitSha`, `engine`, `engineVersion`, `computedAt`, `durationMs`.
`q0Anchor` and `q0Value` are NOT in that list, and `wrap_legacy` does not
route through `stamp_staleness_metadata`. So a `wrap_legacy` producer never
gets a q0 stamp no matter what it imports -- importing `q_parameter` does not
help, which is the thing an agent is most likely to try, because that IS how
the stamp arrives on the `save()` path.

Worked case: `a3_magnitude_parity_orthogonal_probe` imports `q_parameter`,
reads `Q_50_DIGIT_STR`, and its witness still has no `q0Anchor` -- because
line 158 is `WitnessBuilder.wrap_legacy(...)`.

## Why this matters more than the raw percentage

Every q0-anchor audit in the tree keys on `q0Anchor` / `q0Value`. Those audits
therefore see at most 44.7% of the corpus, and report a clean bill on the rest
-- not "unknown", but silence indistinguishable from "fine". The 384 that
demonstrably carry a q0 value in their payload are the actionable subset: they
are provably q0-dependent AND provably unstamped.

Examples (first six found): `chain-binding-closed-form`, `d-from-scratch`,
`multi-level-jet-sum`, `spectral-coordinates-all-atoms`,
`per-irrep-pole-neutron-h3`, `sublemma-2-1-alpha-shift-extract`.

## Not proposing the fix here

Adding a q0 stamp to `wrap_legacy` would change 282 producers' output at once
and is exactly the shape of sweep AGENTS.md says needs scoping first (the
2026-08-19 breakage took `main` red at 208 producers). The measurement is the
deliverable; the sweep is a separate decision.

## Scope note

384 is a LOWER bound on q0-dependence, not the count of q0-dependent
witnesses. It counts witnesses whose payload contains a q0 LITERAL. A witness
that consumes q0 and publishes only derived quantities is q0-dependent and is
not in the 384 -- the same detector-blindness class this bean is about, one
level down.

- **Round 96 (`litlfred/qou#8428`)**: Advanced in `feat/round96-milnororder-signrep-mirrorsplit-multibond-moebius-43c1` (Commit 1 `22d991a251c6bf1bcf86f7ea08f935c2c280b7b3`, Commit 2 `391eb320415cc99c2e005cd0ffab67710cb6bc1d`, probe sha256 `94f6f6be6af6f9daa73f3911e2df79962cba2a56eed95434d4d929e3d5348851`).
