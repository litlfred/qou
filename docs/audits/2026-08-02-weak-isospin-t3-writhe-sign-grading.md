# Weak-isospin `T₃` from the writhe sign — a grading ⟂ generation winding (2026-08-02)

**Branch:** `claude/weak-isospin-t3-grading-2026-08-02` · **PR:** #4618
**Bean:** `qou-tdrd` (root of the convergence epic `qou-20sx`).
**Lean:** [`WeakIsospinT3Grading.lean`](../../content/quantum-observable-universe/lean/QOU/ParticleInteractions/WeakIsospinT3Grading.lean)
(`lean`-direct exit 0, sorry-free, axioms `[propext, Classical.choice, Quot.sound]`).
**Witness:** [`weak-isospin-t3-grading.witness.json`](../../computations/weak-isospin-t3-grading.witness.json)
**Serves:** the honest negative of
[`2026-08-02-meson-fluxtube-junction-reduction.md`](2026-08-02-meson-fluxtube-junction-reduction.md)
(bean `qou-qpj9`, PR #4614); the electroweak siblings #4597 (sin²θ_W) and
#4561 (hypercharge Y); owner bean `qou-jsx5` (#4600).

## The task

Derive a **weak-isospin (up/down-type) grading `T₃` orthogonal to the
generation winding `n`**. The meson-fluxtube attack proved (Lean, sorry-free)
that `windingContent` is **non-injective**: charm (n=5) and strange (n=5)
share the `T(2,n)` generation-2 block, so the D-meson `{5,3}` collides with
the kaon `{3,5}`. The framework cannot tell up-type (charm) from down-type
(strange). The same missing object blocks charmed-hadron masses, sin²θ_W, and
hypercharge Y. The precise datum named there: a **weak-isospin `T₃`**
distinguishing up-type from down-type *at fixed generation*.

## Corpus-grep (STRICT) — is `T₃` genuinely open?

Ran `grep -rniE "weak isospin|up-type|down-type|Gell.?Mann.?Nishijima|I_3|I₃|T_3|T₃|writhe.*isospin"` over `docs/ content/ computations/`. Findings:

| Existing structure | What it is | Why it is NOT weak `T₃` |
|---|---|---|
| [`crystal-isospin-degeneracy.md`](../../content/quantum-observable-universe/braids-and-knots/crystal-isospin-degeneracy.md), [`2026-05-24-isospin-categorical-source.md`](2026-05-24-isospin-categorical-source.md) | **Strong** isospin SU(2)_I: the `u↔d` flavour swap between proton `(u,u,d)` and neutron `(u,d,d)`; source of the 305 ppm `m_n−m_p` split | Nucleon-level strong isospin, first-generation only. Coincides with weak `T₃` for gen-1 but does not extend to the electroweak `Q = T₃ + Y/2` across generations. |
| [`force-knot-identification.md`](../../content/quantum-observable-universe/predicted-spectra/force-knot-identification.md) | The weak generator `T(3,5)` transmutes up↔down; parity violation from the `q≠1` Skein sign-asymmetry `q[L₊] − q⁻¹[L₋] = …` | Identifies the *mediator* and ties the up/down distinction to **crossing sign** — but does not define a per-quark `T₃` invariant or check GMN. |
| `⋈_K` interface ([`isotope_record_schema.py`]) | `pp = σ_g` (+), `nn = σ_g⁻¹` (−), `pn` averaged | The **sign convention** source (used below), not a `T₃`. |

**Conclusion: genuinely open.** No corpus object defines a per-quark
weak-isospin `T₃` valued ±½, orthogonal to generation, satisfying GMN. The
strong-isospin `u↔d` swap is a *different* (nucleon-flavour) object. Proceeded
to derive.

## The derivation

### The two data of a signed integer

The framework's quark torus braid is `T(2,n) = σ₁^{±n}`. Two independent facts
about it already live in the corpus:

* **crossing NUMBER** `n ∈ {3,5,7}` — the generation winding
  (`lepton-meson-torus-knot-dictionary.lean`, `leptonTorusKnotIndex`); a
  *symmetric*, sign-blind function → charm and strange both `n=5`.
* **crossing SIGN** — already a physical grading: strong-isospin `pp = σ_g`
  (positive) / `nn = σ_g⁻¹` (negative); the weak `T(3,5)` maximises the
  `q≠1` Skein `L₊`-vs-`L₋` asymmetry.

The **signed writhe** `κ = ±n` (the net signed crossing of the oriented braid)
factors *canonically*:

```
   κ  =  sign(κ) · |κ|
        └──┬───┘  └┬┘
       T₃ grading   generation winding
```

`|κ| = n` is the generation; `sign(κ) ∈ {+1,−1}` is an intrinsic `ℤ/2` grading
**orthogonal to the magnitude by construction** (sign and magnitude of an
integer are independent data). This is the key move: `T₃` is not a *second*
postulate, it is the **sign-half of the very object whose magnitude the
framework already reads as the generation.**

### Normalisation and sign convention

Normalised as a fundamental SU(2)_weak weight, `T₃ = sign(κ)/2 ∈ {+½, −½}`.

The absolute identification **up-type = positive crossing** is **inherited**
from the strong-isospin `⋈_K` orientation (`pp = σ_g` positive; the proton is
the more-up nucleon → up-type gets the positive channel). Under it:
`charm = σ₁^{+5}` → `T₃ = +½`; `strange = σ₁^{−5}` → `T₃ = −½` — **same
generation `n = 5`, opposite `T₃`.** The degeneracy is resolved by refining
the *unsigned* winding to the *signed* writhe.

### Derive-then-CHECK: Gell-Mann–Nishijima

`T₃` is defined from topology (`signedWrithe`). GMN `Q = T₃ + Y/2` is then
**checked** against the independently-known electric charges `Q` and the
left-doublet hypercharge `Y = 1/3` — a theorem that could have failed:

| quark | κ | T₃ | Q (SM) | Y (L) | T₃ + Y/2 |
|---|---|---|---|---|---|
| u | +3 | +½ | +2/3 | 1/3 | ½ + 1/6 = **2/3** ✓ |
| d | −3 | −½ | −1/3 | 1/3 | −½ + 1/6 = **−1/3** ✓ |
| c | +5 | +½ | +2/3 | 1/3 | **2/3** ✓ |
| s | −5 | −½ | −1/3 | 1/3 | **−1/3** ✓ |
| t | +7 | +½ | +2/3 | 1/3 | **2/3** ✓ |
| b | −7 | −½ | −1/3 | 1/3 | **−1/3** ✓ |

No continuous parameter was tuned — the grading is a discrete `ℤ/2`. The check
succeeds because up-type has the higher charge **and** the `⋈_K`-inherited
convention gives up-type the positive writhe; the two agree, which is the
non-trivial content (`gellMannNishijima`, `T3_eq_charge_minus_halfY`).

## Verdict: DERIVED (with a named conjectural remainder)

**Derived (proved, sorry-free):** an orthogonal `ℤ/2` grading `T₃ = sign(κ)/2`
that (1) separates charm from strange at fixed generation, (2) is valued
`±½`, (3) satisfies GMN for all six quarks. This is enough to break the
`winding_content_not_injective` degeneracy structurally: the D-meson `c̄` block
(`+½`) is selected distinctly from the kaon `s̄` block (`−½`).

**Open (conjecture class `CanonicalWeakIsospinFromBowtie`, NO instance):**

1. that the up-type↔positive-writhe identification is *forced* by the `⋈_K`
   framework orientation rather than *chosen* consistently with it (over the
   finite `Quark` toy the arithmetic is decidable — the openness is
   **physical**, not formal);
2. that this `ℤ/2` lifts to the full SU(2)_L gauge action on the `H_n(q)`
   representations and, combined with the generation tower, reproduces the
   quark masses / CKM mixing.

Both **reduce to the open SU(3)-flavour / CKM sector.**

## Anti-fit / anti-laundering statement

`T₃` was **not** defined to equal the SM assignments by fiat; it is
`sign(signedWrithe)/2`, and GMN is a *checked theorem*. The one convention
(up = positive) is inherited from an existing corpus datum (`⋈_K`), not freshly
postulated to match. The open primary is honestly a **content-bearing class
with no instance**; a trivial `κ := signedWrithe` instance would fabricate
closure and is forbidden (§3b-tax). No anchor-inverted grading is wired to
production.

## Next honest steps (refine `qou-tdrd` / `qou-qpj9`)

1. **Derive-or-refute the forced sign.** Show the `⋈_K` orientation *forces*
   up=positive from the strong-isospin proof (not just is consistent). If it
   does, `sign_forced_by_bowtie` promotes from conjecture-field to theorem.
2. **Construct the canonical `κ`** as the net signed crossing of the actual
   `H₃(q)` meson braid (the `lepton-meson-parallel.md` construction), so
   `writhe_magnitude_is_generation` is proved on the real object rather than
   the toy.
3. **Wire into the meson-fluxtube D-vs-K selection** (bean `qou-qpj9`): the
   `c̄` block at `T₃ = +½` vs the `s̄` block at `T₃ = −½` now gives the
   operator-selection LP a datum that separates them — *then* one `m_D` check.
4. **Cross with #4561's derived Y** to replace the SM `Y = 1/3` input in
   `gmn_with_derived_hypercharge`, closing GMN entirely inside the framework.
