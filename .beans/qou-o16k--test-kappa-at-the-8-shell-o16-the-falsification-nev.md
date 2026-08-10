---
# qou-o16k
title: 'Test κ at the 8-shell (¹⁶O) — the falsification the anchor-identified form has never faced'
status: in-progress
type: task
created_at: 2026-08-10T02:32:00Z
updated_at: 2026-08-10T03:05:00Z
---

## Result (2026-08-10) — the test is sharper than expected, and partly blocked

[`probe_kappa_shell8_excess_convention.py`](../computations/probe_kappa_shell8_excess_convention.py)
→ `kappa-shell8-excess-convention.witness.json`, 4/4 assertions. No fit, no
tuning; arithmetic only.

**The κ fit is convention-blind by construction.** The corpus carries two
inequivalent definitions of the excess `(n_pp − n_nn)`:

| | definition | in Z |
|---|---|---|
| **C1** | `def:canonical-braid-interface-composition` — `n_pp = max(0, Z−1)` | linear |
| **C2** | `prop:derived-mass-formula-light-isotopes` — `n_pp = Z(Z−1)/2` | quadratic |

They **agree on every anchor κ has ever seen** and diverge everywhere else:

| nuclide | Z | N | shell | C1 | C2 | C2/C1 | role for κ |
|---|---|---|---|---|---|---|---|
| ³He | 2 | 1 | 2 | 1 | 1 | 1× | cross-check |
| ³H | 1 | 2 | 2 | −1 | −1 | 1× | cross-check |
| ⁴He | 2 | 2 | 2 | 0 | 0 | — | identification |
| ¹⁵O | 8 | 7 | 8 | 1 | **7** | **7×** | never tested |
| ¹⁵N | 7 | 8 | 8 | −1 | **−7** | **7×** | never tested |
| ³⁹K | 19 | 20 | 20 | −1 | **−19** | **19×** | never tested |

So the fit that fixed κ **could not have distinguished the two conventions** —
it lives entirely inside the region where they coincide. Since `kappa_closed`
carries **no shell index** (it is a function of `q` and `m_e` alone, verified),
the conjecture predicts one constant for every shell, and that constant
multiplies an excess that differs by 7× at shell 8 depending on which
convention is meant. The block does not say which.

That is a second defect, independent of the anchor-identification one: even
granting the closed form, **the conjecture is not yet a determinate statement**
until the convention is named.

## Blocked, and stated rather than guessed

Extracting an *observed* slope at the 8 shell needs the binding decomposition
the removed producer `probe_kappa_categorical_h7a_closed.py` carried. Checked:
the naive route (mirror-pair ΔB over Δexcess for ³He/³H) gives −0.382 MeV,
about 2.8× off `κ_emp = −1.0708`, so κ is plainly not a bare mirror-pair slope
and other terms are in play. **Reconstructing that decomposition by guesswork
would be a new fit** — precisely what the demotion was about. Blocker recorded
instead.

## Next

1. **Name the convention** in the block — a one-line fix that makes the
   conjecture determinate, and a prerequisite for any 8-shell test. Requires an
   owner call on which of C1/C2 κ was fitted against; the anchors cannot say.
2. **Recover the binding decomposition** (git history of the removed producer),
   then run the 8-shell prediction with no re-tuning.
3. Corroboration for the premise, from the corpus itself:
   `def:canonical-braid-interface-composition` already states *"A linear fit
   across the interfaces evaluates the 4-atom set, requiring evaluation against
   larger $A$ to verify structural predictions."*

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
