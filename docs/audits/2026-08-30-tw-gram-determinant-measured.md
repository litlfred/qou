# The `T_w` Gram determinant, measured at ranks 1–3 — and what it forecloses

*2026-08-30, bean `qou-0y6h`. Probe:
[`computations/hecke/tw_gram_determinant_probe.py`](../../computations/hecke/tw_gram_determinant_probe.py).*

## Why this was measured before formalising

`QOU.Hecke.TwBasis` reduces semisimplicity of `H_n(q)` at every rank to
`det (twGram) ≠ 0`, and closes that determinant at `n = 1`
(`twGram_det_rank_one : det = (1+q)²`, sorry-free). The remaining content of
`qou-0y6h` is the determinant at higher rank. Formalising a determinant one does
not know the value of is the expensive way to discover it, so the value was
measured first — a cheap exact computation, ~12 s, against the formalize-first
rule's own caveat that a decisive cheap probe beats a hard formalisation.

## The measurement

Exact integer / symbolic arithmetic throughout; no float appears and none is
admissible (the output is an argument, not a digit).

| `n` | algebra | `det (twGram K q n)` |
|---|---|---|
| 1 | `H_1(q)`, `S₂`, dim 2 | `[2]_q²` |
| 2 | `H_2(q)`, `S₃`, dim 6 | `− 2⁴ · q² · [2]_q² · [3]_q⁶` |
| 3 | `H_3(q)`, `S₄`, dim 24 | `− 2⁴·3¹⁸ · q²² · [2]_q²⁸ · [3]_q⁶ · [4]_q²⁰` |

**The integer constant is exactly `∏_λ d_λ^{d_λ²}`**, over the partitions of
`n+1`, `d_λ` the number of standard Young tableaux:

    S₂: 1,1        →  1
    S₃: 1,2,1      →  2⁴          = 16
    S₄: 1,3,2,3,1  →  2⁴·3¹⁸      = 6198727824

### How firmly

* **`n = 1` reproduces a Lean theorem.** `twGram_det_rank_one` is proved
  sorry-free, so the probe's arithmetic is validated against a result it did not
  produce, rather than against itself.
* **`n = 2` is symbolic** — sympy over `ℚ(q)`, no fitting; the `16` comes out
  of the determinant directly.
* **`n = 3` is a polynomial identity, not a sample.** The row-degree bound on
  the `24 × 24` determinant is 216 and the candidate has degree 122, so
  agreement at 298 integer values of `q` forces equality.

## Consequence 1 — the shape confirms the bean's target

`qou-0y6h` names `det(Gram) = ∏ Schur`. The structural reading — **not proved
here, stated as the reading that predicts the data** — is that the regular trace
is the symmetrizing trace twisted by the central element
`z = Σ_λ d_λ s_λ e_λ`: from `tr(L_x) = Σ_λ d_λ tr_λ(x)` and
`τ = Σ_λ s_λ⁻¹ tr_λ` one gets `regForm(x,y) = τ(z·x·y)`, hence

    det(regGram) = det(τGram) · det(L_z) = ± q^{Σ_w ℓ(w)} · ∏_λ (d_λ s_λ)^{d_λ²}.

That reading predicts the integer constant `∏ d_λ^{d_λ²}`, and the prediction
matches at `n = 2` with no fitting at all. The `q`-exponents are *not* `Σ_w ℓ(w)`
as written (9 and 72 against the measured 2 and 22), because the `s_λ` carry
`q`-powers of their own; the factorisation into `[k]_q` is also not canonical
(`[4]_q = [2]_q(1+q²)`), so read the table as a value, not as a normal form.

## Consequence 2 — the route is one-directional, and this is the finding

**The constant is `> 1` for `n ≥ 2`, so in a characteristic dividing it the
determinant vanishes even where `H_n(q)` is semisimple.** For `A = M_d(K)` the
regular trace form is degenerate exactly when `char K ∣ d`; the constant is the
product of those obstructions across the Wedderburn blocks. So

    det(twGram) ≠ 0  ⟹  H_n(q) semisimple

is all this route can ever give. The converse is **false**, and stating the
general theorem as an iff would be wrong. Concretely: over a field of
characteristic 2 with `q` of multiplicative order > 3, `[2]_q`, `[3]_q` and `q`
are all nonzero while `2⁴ = 0`, so `det = 0` at `n = 2` — and Dipper–James still
gives semisimplicity there.

Practical consequences:

* Any general Lean theorem along this route must carry a **characteristic**
  hypothesis. The corpus's `QGeneric q n` framing (`q^k ≠ 1`) does not supply
  one, and would be an incorrect hypothesis set on its own.
* For the substrate case — `K = ℝ`, `q > 1` — the constant costs nothing, and
  `isSemisimpleRing_rank_one_of_pos` is already in that shape.
* An agent hoping to get a **characteristic-free** converse (semisimple ⟹
  det ≠ 0, i.e. a clean criterion over any field) should stop: it is false, and
  the counterexample is above.

  > **🛑 SCOPED 2026-09-03 — the converse IS true in characteristic zero, and
  > is now proved.** This bullet read *"an agent hoping to get the converse
  > should stop: it is false"*, unqualified. The **counterexample above stands
  > and is unamended** — it is at characteristic 2, and nothing here weakens
  > it. But the unqualified sentence closes a route this very audit leaves open
  > two paragraphs up (*"any general Lean theorem along this route must carry a
  > characteristic hypothesis"*, and *"it is not a claim that the determinant
  > route fails in characteristic 0"*).
  >
  > `QOU.Hecke.TwBasis.twGram_det_ne_zero` proves `det (twGram K (q^2) n) ≠ 0`
  > over any `[Field K] [CharZero K]` with `q` not a root of unity, at **every**
  > `n`, sorry-free — i.e. exactly the characteristic-carrying theorem this
  > audit predicted. It runs the implication backwards: semisimplicity comes
  > from `heckeWedderburn`, which owes the Gram determinant nothing, and the
  > converse Gram criterion turns that into `det ≠ 0`. See
  > [`2026-09-03-gram-converse-in-characteristic-zero.md`](2026-09-03-gram-converse-in-characteristic-zero.md).
  >
  > Recorded because this is the AGENTS.md over-narrowing failure in miniature:
  > the measurement was right, the scope sentence was one clause short, and that
  > clause was the one a later agent would act on.
  >
  > Independent corroboration, worth noting since it runs the other way: this
  > audit derives the obstruction as *"`M_d(K)`'s regular trace form is
  > degenerate exactly when `char K ∣ d`"*, and the new Lean's
  > `regTraceForm_one_one` gives `B(1,1) = finrank K A`, which for `M_d(K)` is
  > `d²`. For prime `p`, `p ∣ d²` iff `p ∣ d`. The two agree, by completely
  > different arguments.

## Scope note on the negative

This is a **scope-(b) structural exclusion** in the sense of AGENTS.md, and the
invariant is cited: the regular trace form of `M_d(K)` is degenerate when
`char K ∣ d`, so no computation of `det(twGram)` can certify semisimplicity in
those characteristics. It is *not* a claim that the determinant route fails in
characteristic 0, where it remains the live route and is the content of
`qou-0y6h`.

## What is still open

> **🛑 UPDATED 2026-09-03 — non-vanishing is CLOSED; the VALUE is what remains.**
> This section's title claim, *"`det(twGram)` at rank ≥ 2 in Lean"*, is now
> ambiguous and half-done. `det ≠ 0` is proved at every rank in characteristic
> zero (`twGram_det_ne_zero`, above). The paragraph below is still exactly right
> about the **value** — `[T_u T_w : T_w]` still has no closed form in the corpus,
> and the `S₅` witness of
> [`2026-09-02-tw-regular-trace-not-combinatorial.md`](2026-09-02-tw-regular-trace-not-combinatorial.md)
> still closes the combinatorial search for one. It is only wrong that
> non-vanishing waits on it: it does not, because it does not go through
> `tr(L_{T_u})` at all.

`det(twGram)`'s **value** at rank ≥ 2 **in Lean**. Knowing the value does not supply the
proof: the Gram entries are `tr(L_{T_v T_w})`, and the general diagonal
structure constant `[T_u T_w : T_w]` still has no closed form in the corpus. The
generator case is proved (`trace_lmul_σ`, `two_mul_trace_lmul_σ`) and does not
imply the rest — at `q = 1` the trace is `δ_{u,1}(n+1)!`, but at generic `q` the
`u = s_i` case is `(q−1)(n+1)!/2`, so it is not concentrated at `u = 1`.
