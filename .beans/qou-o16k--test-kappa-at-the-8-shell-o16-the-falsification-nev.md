---
# qou-o16k
title: 'Test κ at the 8-shell (¹⁶O) — the falsification the anchor-identified form has never faced'
status: todo
type: task
created_at: 2026-08-10T02:32:00Z
updated_at: 2026-08-10T02:32:00Z
---

Follow-up to `qou-k4dm`. Answers the owner's question *"deprecated magic shell —
did any align with 8-fold? anything in paper corpus to relook at?"*

## The 8-fold question: no

Checked numerically. The magic-shell slope needs a normaliser

    N = E₀·log(1/h) / |κ_obs| = 6.118482

against which every octet-flavoured candidate is far away:

| candidate | value | rel. err |
|---|---|---|
| `[2]_q[3]_q` — the current fit | 6.120579 | **0.034 %** |
| `[2]_q + [4]_q` | 6.120579 | 0.034 % |
| flat 6 | 6 | 1.94 % |
| `[6]_q` | 6.388087 | 4.41 % |
| flat 8 | 8 | 30.75 % |
| `[2]_q³` | 8.131476 | 32.90 % |
| **`[2]_q[4]_q` — sl₃ adjoint, the OCTET** | 8.264148 | **35.07 %** |
| `[8]_q` | 8.945690 | 46.21 % |

The corpus's octet is `V_(2,1)` at `dim = 8` in the `n = 3, N = 3` quantum
Schur–Weyl decomposition (`content/.../eightfold-way/schur-weyl-eightfold.md`),
and it carries the same 8, so the same ~35 % mismatch. **The octet does not
normalise κ**, and no rescue is close.

## One structural reading worth recording

`[2]_q·[3]_q = [2]_q + [4]_q` **exactly** — verified to machine precision above,
and it is the sl₂ fusion `V₂ ⊗ V₃ ≅ V₂ ⊕ V₄`. So κ's normaliser is a *sum over
fusion channels*, the doublet plus the quartet, not an opaque product. The block
currently calls it "the quantum dimension of the `V₂ ⊗ V₃` Schur–Weyl tensor
product", which is loose: the eightfold chapter's Schur–Weyl decomposition is the
gl₃ one with dims 10/8/1, a different object that happens to share the name.
Worth stating the fusion form — a derivation is likelier to produce a channel sum
than a product.

## The actual relook: κ has never met a second shell

`compound-beta-shell-calibration` — κ's own parent — declares the magic anchors
`A_magic ∈ {2, 8, 20, 28, 50, 82, 126}`. κ was **identified** at (2,2) = ⁴He and
**cross-checked** at (2,1)/(1,2) = ³He/³H. Every one of those sits in the
`A_magic = 2` shell.

**The 8 shell has never been evaluated.** ¹⁶O (Z = N = 8) is doubly magic, is
already named in the corpus, and is the obvious falsification test: a form fitted
in one shell either predicts the next shell or it does not. Running it costs
nothing and settles the conjecture's standing in one direction or the other.

Do it as a *prediction*, not a fit — compute `κ` from the closed form at the
8-shell anchors and compare, with no re-tuning permitted. Either outcome is
publishable: agreement is the first genuine evidence the form is derived,
disagreement scopes the conjecture to the 2-shell (a scope-(a) negative, per the
refutation-scoping rule — not a structural exclusion).

## Two adjacent gaps found while looking

Both flagged live by `run-validate` right now, both in `eightfold-way/`:

- `prop:meson-octet-decomposition` — no Lean declaration
- `prop:borromean-decuplet` — no Lean declaration

The eightfold chapter's two central claims are unformalised. Separate work, but
they are the formal backing any octet-route attack on κ would need.
