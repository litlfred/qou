# z→c_k f-map — B3 u-side transfer scope (bean `m9j4`, multi-session)

**Date:** 2026-07-07 · **Follows:** the merged z→c_k tranche (PR #3449, KC13–KC16).
· **Ledger:** [`z-ck-fmap-keystone.md`](../coordination/z-ck-fmap-keystone.md)
· **Standing reading:** parity gates test the bar-odd part, shadow gates the
bar-even part (owner-granted 2026-07-07; registry KC6/KC10).
· **Discipline:** SCOPE ONLY — no probe run here; kill criteria pre-stated for
the next tranche. No c_k value, no wiring, no tier change.

## 1. What is proved (fibre level) vs what is open (u-side)

The merged tranche established the parity structure of the f-map's *fibre*
ingredients, all machine-certified:

| result | statement | tier |
|---|---|---|
| KC13 | `z = √q/(1+q)` exactly bar-even; `κ_{(2,1)}` exactly bar-odd | proved-lean |
| KC15 | `D(q) = α₁(q,φ²) − α₁(q,φ⁻²)` exactly bar-odd, `D(1) = 0` | proved-lean |
| KC16 | one-sided Habiro basis `(q;q)_k` index-alternating: even k ↔ bar-even, odd k ↔ bar-odd, twist `q^{−k(k+1)/2}` | proved-lean |
| ZBarParity §2 | `ℏ_q = 1 − q⁻¹` bar-odd (twist `−q`); `ℏ_q²` bar-even (twist `q²`) | proved-lean |

**The open object** is the *transfer*: the observable ladder lives in
`u = b·ℏ_q²`, and the `c_k` are its coefficients via the Habiro
`(u;u)_m → u^k` change of basis
(`prop:q-beta-c-k-recursion-from-habiro-q-difference`). The fibre bar
involution is `q ↦ q⁻¹`; the question is what it becomes as an action on the
`u`-adic filtration, and whether the KC16 index-parity survives the basis
change to give the `c_k` their even/odd structure.

## 2. The transfer map's bar-compatibility (the one structural handle)

`u = b·ℏ_q²` with `b` bar-fixed. From `hbar_sq_bar_even_twist`:

```
bar(u) = q² · u        (bar-even up to the monomial twist q²).
```

So the bar involution does **not** fix `u` pointwise — it scales it by `q²`.
Consequences to formalize:

1. **`u`-monomials carry a bar-twist that grows with degree:**
   `bar(u^k) = q^{2k}·u^k`. The `u`-adic grading is therefore bar-compatible
   *up to a degree-dependent monomial* — the same shape as the KC16 Gauss-sum
   twist `q^{−k(k+1)/2}` on `(q;q)_k`. The transfer is the composition of
   these two twists; the open question is whether they **cancel to a clean
   index-parity** on the `c_k`.
2. **The `(u;u)_m` Habiro basis vs the KC16 one-sided `(q;q)_k`:** the ladder
   basis `(u;u)_m = ∏_{j=1}^m (1 − u^j)` is built from `u`, not `q`. Under
   `bar(u) = q²u` it is **not** the same object as `(q;q)_k`; the two are
   related by the `q ↦ u` substitution that IS the transfer map. Making that
   substitution explicit — and tracking the twist — is step B3-U1.

## 3. Pre-stated gates for the next probe (B3-U, decidable, exact)

- **B3-U1 (basis image):** compute `(u;u)_m` for m = 1..6 with `u = b·ℏ_q²`,
  re-expand in `q`, and check whether its bar-image `(bar(u);bar(u))_m` equals
  `(q²u; q²u)_m` with a clean monomial twist (analogue of KC16). Kill: no
  monomial twist ⇒ the u-side basis is not bar-graded and the fibre parity
  does **not** transfer cleanly.
- **B3-U2 (parity descent):** under the `(u;u)_m → u^k` change of basis
  (Habiro coefficients), track whether an index-`m` bar-odd basis vector
  contributes to bar-odd `c_k` only. Kill: parity leaks across the change of
  basis ⇒ the KC16 mechanism does not survive to the observable ladder.
- **B3-U3 (D(q) placement):** identify which `u`-rung `D(q)`'s bar-odd content
  lands on after transfer — the candidate is `c_3` (the first bar-odd rung,
  `c_3 → −2` shadow via the even part per the standing reading). Kill: `D(q)`
  transfers to an even rung or spreads across all rungs ⇒ not the `c_3` source.
- **Standing-reading gate:** every parity claim tests the bar-odd PART; every
  shadow claim (`c_2 → −1`, `c_3 → −2`) tests the bar-even PART. A candidate
  asserting a q=1-regular rung is exactly bar-odd with nonzero shadow is
  auto-rejected (fixed-point rule; validator R3).

## 4. Why this is the remaining keystone, honestly

Everything up to the fibre↔archimedean wall is now proved parity structure.
The `u`-side transfer is the **only** step that crosses the wall: `u` is a
real archimedean composite, and the bar involution acts on it *with a
degree-dependent twist* rather than fixing it. Whether the fibre index-parity
(KC16) + the bar-odd carrier `D(q)` (KC15) descend to give the `c_k` their
observed structure — or whether the twist obstructs the descent — is the open
question. It is decidable in exact symbolic form (§3), but it is genuinely
multi-session: the `(u;u)_m → u^k` coefficients grow in `q`-degree, and the
descent must be tracked rung-by-rung. No `c_k` value is claimed here; a clean
descent would still be a *structural* identification of the odd channel, not
an anchor-validated coefficient (precision floor: only `c_2, c_3` are
data-determined).

## 5. Cross-references

- Fibre parity certificates: [`ZBarParity.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/ZBarParity.lean) §2/§6/§7
- Transfer map (open): [`prop:q-beta-c-k-recursion-from-habiro-q-difference`](../../content/quantum-observable-universe/mass-theory/q-beta-c-k-recursion-from-habiro-q-difference.md)
- Registry: [`ck-dk-canonical-registry.md` §9](../coordination/ck-dk-canonical-registry.md) (KC13–KC16)
- Quantum-modular S-shadow framing: [2026-06-13 heat f-map audit](../audits/2026-06-13-qbeta-heat-fmap-symbolic-and-literature.md) §2-quater
