
---

## 2026-10-10 — ITEM 3 SETTLED: the supergolden root IS a convention-C artefact, by exact division

Re-audit of the C→D migration tracker (session epic `qou-am5t`). This bean's
item 3 said the question was *"answerable directly from the generic form"*. It
is, and the answer is unambiguous. Probe:
[`computations/probes/gram_h3_supergolden_is_convention_c_artefact_probe.py`](../../computations/probes/gram_h3_supergolden_is_convention_c_artefact_probe.py)
— **6/6 checks, exit 0**, witness
`computations/probes/gram-h3-supergolden-is-convention-c-artefact.witness.json`.

### The answer

Taking the generic factorisation this bean records,
`det = −(z−q)⁵(qz+1)⁵((q²+1)z − q³)(q³z + qz + 1)/q⁸`, and substituting each
convention's `z`:

| factor | under C (`q = u²`, `z_C = u/(u²+1)`) | under D (`z_D = q³/(q²+1)`) |
|---|---|---|
| `(z − q)` | **`−u(u³ + u − 1)/(u²+1)`** | `−q/(q²+1)` — **no positive root** |
| `(qz + 1)` | `(u³ + u² + 1)/(u²+1)` — no positive root | `(q²−q+1)(q²+q+1)/(q²+1)` — none |
| `((q²+1)z − q³)` | `−u(u−1)(u⁶+u⁵+2u⁴+u³+u²+u+1)/(u²+1)` | **`0` identically** |
| `(q³z + qz + 1)` | `(u+1)(u⁶−u⁵+u⁴−u³+2u²−u+1)/(u²+1)` | `q⁴+1` — none |

**The supergolden cubic is the numerator of `(z − q)` under convention C,
exactly.** Dividing `numer(z_C − q) = −u(u³+u−1)` by `u³+u−1` gives quotient
`−u` and remainder **0** in `ℚ[u]`. That is the whole verdict, and it is an
exact polynomial identity — not a numerical zero.

**Under D the same factor is nowhere zero.** `z_D − q = −q/(q²+1)`, whose
numerator `−q` has no positive root; at `q = (1/ψ)²` it is `−0.3826…`.

**The two frames' det-vanishings have DISJOINT mechanisms**, which is the part
that settles the physics reading:

- **C** vanishes through `(z−q)⁵` at `u = 1/ψ ≈ 0.6823278038280193…`.
- **D** vanishes through `((q²+1)z − q³) ≡ 0` — the Markov-parameter relation
  itself, i.e. `markovWeightD_root`, the declaration this bean records as
  added "so a later relabel cannot silence it". Under C *that same factor*
  vanishes on `u > 0` only at `u = 1`, i.e. `q = 1`, the classical point —
  **not** the supergolden value.

So neither threshold is the other's image. `1/ψ` is the root that writing `z`
in convention C creates in the factor `(z − q)`; it has no D-frame counterpart.

### Why the verdict does NOT rest on the obvious numerical check

Evaluating `z_C − q` at a float64 root of `u³+u−1` returns `5.55e-17`. That is
the floor of float64, and reporting it as agreement would be precisely the
practice AGENTS.md forbids — *"never report a float64 agreement as exact,
identical, or to N digits"*. The probe records it only to say why it is not
the evidence. The evidence is check 1's exact division.

### Scope: (a), NOT (b) — and this is the part that matters for item 2

This is **not** a structural exclusion of a supergolden feature anywhere in
the framework. It is the narrower claim that *this* threshold, in *this*
determinant, is an artefact of *this* substitution.

**But it does change the standing of item 2's second option.** This bean
offers, as an honest disposition of `prop:spectrahedral-phase-collapse`,
re-deriving "whether some other D-frame object (the Gram on the radical
quotient, which `gram-matrix-dual.witness.json` already carries as
`gram_quotient_inverse`) has a supergolden rank drop, which would be a real
result rather than a relabel." That search is still permitted — nothing here
forbids it — but an agent taking it should know it is **looking for a new
result, not recovering an old one**: the supergolden value is not a
frame-independent feature of the Gram determinant, so there is no prior reason
to expect it to reappear. Expecting it would be selection against a target the
measurement has just removed.

### What this does NOT settle, and is not mine to settle

- **Item 1 (the `gramMatrix` → `gramMatrixC` / `gramMatrixD` rename)** —
  untouched. ~15 declarations and one downstream importer; it belongs with
  item 2 as this bean says.
- **Item 2 (what the content block should say instead)** — untouched. That is
  authoring in a second content block and is an owner call. The measurement
  above is an input to it, not a decision.
- The **convention-C theorems are correct theorems about a non-canonical
  frame** and are not touched. Per AGENTS.md a Lean-proved piece is a
  permanent contribution; this probe scopes a *reading*, not a proof.
- The probe **consumes** the generic factorisation from this bean and
  `gram_h3_convention_frame_probe.py`; it does not re-derive the determinant.

### Status

Staying `todo`: items 1 and 2 are open and both need the owner. Item 3 is
closed with a probe and a witness.

Reproduce:

```sh
python3 computations/probes/gram_h3_supergolden_is_convention_c_artefact_probe.py
```
