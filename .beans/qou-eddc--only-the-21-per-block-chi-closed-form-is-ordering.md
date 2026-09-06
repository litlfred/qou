---
# qou-eddc
title: Only the (2,1) per-block chi closed form is ordering-dependent; the q^2-1 vanishing survives
status: in-progress
type: task
priority: normal
created_at: 2026-09-06T13:05:29Z
updated_at: 2026-09-06T13:05:55Z
---

## Measured

`Δ_{T_β} = χ_λ(β_n) − χ_λ(β_p)` at the proton pin, 50 dps, under both orderings,
against the closed forms in
`content/quantum-observable-universe/lean/QOU/BraidKnot/QBetaPerBlockChiClosedForms.lean`
(lines 72–99):

| λ | paper closed form | **grouped** | **borromean (canonical)** |
|---|---|---:|---:|
| (3) | $-(q^2-1)(q^2+1)^2/(4q)$ | −0.26038764179012 | −0.26038764179012 |
| (2,1) | $(q^2-1)(-q^4-1)/(4q^3)$ | −0.10681445765158 | **−0.09136297383787** |
| (1,1,1) | $-(q^2-1)(q^2+1)^2/(4q^5)$ | −0.17153864377660 | −0.17153864377660 |

    paper forms reproduce from GROUPED words   : True
    paper forms reproduce from BORROMEAN words : False   (one block only)

**Exactly one of the three is ordering-dependent, and it is the only
2-dimensional block.** (3) and (1,1,1) are the one-dimensional
representations — the generators act by scalars there, so they commute and the
intra-ordering cannot matter. (2,1) is 2-dimensional, where σ₀ and σ₁ genuinely
do not commute.

That is the `qou-hu1f` ruling's own stated reason (*σ₀ and σ₁ do not commute, so
only the alternating word is β_Bor*) reappearing from a direction that did not
assume it: the ordering moves the answer precisely where non-commutativity is
visible, and nowhere else. Worth noting as independent support for the ruling.

## What survives, and it is the load-bearing part

The content block `qbeta-per-block-delta-tau-intro.md` does not rest on the
polynomials; it rests on their **vanishing at the classical point**:

> The per-block characters χ_λ(Δ_{T_β})(q) … vanish at the classical point
> q = 1 … this vanishing forces the trace difference Δtr_M to carry an explicit
> (q²−1) factor

Measured on the borromean (2,1) block as q → 1 along irrational points:

| q − 1 | Δ_(2,1) | Δ/(q²−1) |
|---:|---:|---:|
| 3.14e-6 | −3.1416e-6 | −0.49999842916 |
| 3.14e-4 | −3.1411e-4 | −0.49984247653 |
| 3.14e-2 | −3.0638e-2 | −0.48007006777 |

So the borromean block **also** carries the (q²−1) factor, and its leading
coefficient is **−1/2** — the same limit the paper form gives
($(q^2-1)(-q^4-1)/(4q^3)$ → $-2/4$ at q = 1). The two orderings agree on the
vanishing and on the leading coefficient; they differ only at higher order.

**So nothing downstream of the vanishing is affected.**
`prop:qbeta-delta-tau-canonical-conditional-q2-minus-1-factor` and the Taylor
data feeding the c_k recursion rest on the factor, which holds either way.

## What needs doing

Restate **one** closed form, `(2,1)`, under the canonical ordering — in
`QBetaPerBlockChiClosedForms.lean` and wherever the block quotes it. The other
two are correct as written and must not be touched.

I have not derived the borromean (2,1) polynomial; only its value at q₀
(−0.091362973837869) and its q → 1 behaviour. Deriving it symbolically is the
work here.

## Scope note

`probes/qbeta_delta_vs_deltaTbeta_settled_probe.py` verifies the paper forms and
is pinned to `intra_order="grouped"` (bean `qou-y2o7`), correctly: its whole
comparison is in that frame. Once the (2,1) form is restated, that probe should
gain a canonical arm rather than being flipped — the grouped arm still records the
historical agreement it was written to guard.

Found while running that probe for the first time in this container: it carried
hardcoded `/home/user/qou/computations` sys.path entries, so every import raised
`ModuleNotFoundError` here and it had never executed. Fixed to derive from
`__file__` (`qou-y2o7`), which is how this became measurable at all.

---

## DERIVED (2026-09-06)

$$\chi_{(2,1)}(\Delta_{T_\beta}) = \frac{(q^2-1)(q^4+1)\,P(q)}{4q^{9}},
  \qquad P(q) = 2q^{12}-5q^{10}+5q^{8}-5q^{6}+5q^{4}-5q^{2}+2$$

Derived symbolically from `atom_canonical_crossings(Z,N)` through
`hecke_character_symbolic.q_character_on_braid_word` — from the words, not
fitted to samples. Probe + witness:
`computations/qbeta/qbeta_per_block_chi_borromean_closed_forms_probe.py`,
8/8 assertions.

The other two came back **provably identical** to the published forms (sympy
difference exactly 0), confirming the dimension argument rather than assuming
it:

| λ | dim | canonical vs published |
|---|---:|---|
| (3) | 1 | IDENTICAL |
| (2,1) | 2 | **differs** |
| (1,1,1) | 1 | IDENTICAL |

### Relation to the published form, and why the classical point is safe

    canonical / published = -P(q)/q^6,     P(1) = -1,     P palindromic

`P(1) = -1` is the whole reason the classical-point results survive: the two
forms **agree exactly at q = 1**. Verified symbolically, not sampled:

- `(q²−1)` factor present in both;
- `lim_{q→1} χ_(2,1)/(q²−1) = −1/2` in **both** frames (sympy `limit`, not a
  numerical approach);
- both are **odd** polynomials in `h = q − 1/q` — bar-parity preserved:

      published   −h³/4 − h/2                                  (degree 3)
      canonical    h⁹/2 + 11h⁷/4 + 17h⁵/4 + 5h³/4 − h/2        (degree 9)

`P` palindromic (`q¹²·P(1/q) = P(q)`) is the consistency check that depends on
no numeric pin at all.

So `chi_block_vanishing_at_one`, `prop:qbeta-delta-tau-canonical-conditional-q2-minus-1-factor`
and the Taylor data feeding the `c_k` recursion are unaffected in substance.

## Lean: marked, NOT migrated — and why

`QBetaPerBlockChiClosedForms.lean` now carries the canonical form, the factor,
and what survives, in `chi_block_21`'s docstring. **The definition is
unchanged** (diff is 30 insertions, 0 deletions).

That is deliberate. `chi_block_21` carries proof obligations in a 1182-line
file and is referenced by seven others, and I cannot compile Lean here to check
a re-derivation — `qou-lsib` records that content-block Lean siblings do not
build. Changing a definition whose proofs I cannot verify is the one thing this
arc has been careful not to do.

### The migration, enumerated

- [ ] `chi_block_21` — swap in `(q^2-1)*(q^4+1)*P q / (4*q^9)`
- [ ] `chi_block_vanishing_at_one` (line ~107) — `unfold; norm_num`; the
      `(q-1)(q+1)` factor is still explicit, so this should go through
- [ ] the `chi_block_21 q = (q^2 - 1) * P21 q` factorisation (line ~152) —
      **`P21` itself changes**: from `(-q^4-1)/(4q^3)` to
      `(q^4+1)*P q/(4q^9)`. This is the real work.
- [ ] the two downstream weighted sums (lines ~235, ~1091) — reference only,
      should typecheck unchanged, but their *values* move
- [ ] seven referencing files: `QBetaCanonicalMarkovWeightsInstance.lean`,
      `qbeta-delta-tau-canonical-conditional-q2-minus-1-factor.lean`,
      `qbeta-per-block-chi-closed-forms.lean`, `qbeta_hecke_mn_character_engine_probe.py`,
      `qbeta_utils.py`, `qbeta_reeb_tower_jacobi_anger.py`
- [ ] `qbeta_delta_vs_deltaTbeta_settled_probe` — add a canonical arm; do NOT
      flip its grouped arm, which records the historical agreement it guards

Blocked on being able to build the Lean. Everything numeric it needs is done.
