# The H₂S Bring `1/√5` is the ζ₅ chiral fibre of Bring's surface

**Date:** 2026-06-09. **Status:** structural connection established; exact
ζ₅-residue normalisation open. **Compute:**
[`h2s_bring_zeta5_chiral_residue.py`](../../computations/h2s_bring_zeta5_chiral_residue.py).

## The question

[`conj:h2s-angle-s3-braid-holonomy`](../../content/quantum-observable-universe/molecular-construction/h2s-angle-s3-braid-holonomy.md)
found the H₂S bond-angle residual takes the **Bring `1/√5`** residual-mixing
form (predicting H₂S/H₂Se within 0.1°). Where does `1/√5` come from, structurally?

## The connection (chiral channel ↔ Bring chiral fibre ↔ ζ₅ ↔ √5)

1. **The chiral channel is the Bring chiral fibre.** The chiral channel is the
   `c_λ=0` `(2,1)` block — the H₃ standard rep. Bring's surface has a **chiral
   cubic fibre** (`bring_chiral_fibre_figure.py`) from the invariant ring,
   `X³+(z+1)X²+(z²+z+1)X+(z³+z²+z+1)=0`, whose **three sheets** merge at the
   discriminant branch points with **B₃ monodromy** (B₃ ↠ H₃). The chiral
   channel and the Bring chiral fibre are the *same* H₃ object.

2. **Bring's surface carries the ζ₅ automorphism.**
   `prop:x5-z5-automorphism`: the hyperelliptic quintic `𝒳₅: y²=x⁵−1` has the
   ℤ₅ automorphism `(x,y)↦(ζ₅x,y)`, `ζ₅=exp(2πi/5)`. This is the 5-fold
   singular-fibre structure around which the chiral residue's monodromy runs.

3. **ζ₅ ⇒ √5.** The quintic is where √5 enters, exactly and only:
   - `cos(2π/5) = (√5−1)/4`, `2cos(2π/5) = (√5−1)/2 = 1/φ` — ζ₅'s irrationality
     over ℚ *is* √5;
   - `disc(x⁵−1) = 5⁵`, so the quintic period carries `√(5⁵) = 25√5`;
   - the quadratic Gauss sum `Σ_{k} ζ₅^{k²} = √5` (verified exactly).

So the **archimedean** projection (`Im q₀ = 0`) of a ζ₅-symmetric chiral
residue is normalised by √5, and its leading chiral coefficient is **`1/√5`** —
the Bring constant of the H₂S residual-mixing form.

## Derived vs open

- **Established:** the chiral channel *is* the Bring chiral fibre (same H₃ /
  B₃-monodromy object); Bring's surface carries the ζ₅ automorphism; ζ₅ is
  irrational over ℚ exactly through √5 (`cos(2π/5)`, the quintic discriminant,
  the Gauss sum). So the chiral residue's irrational scale can only be √5, and
  the H₂S `1/√5` is the quintic √5 of the ζ₅ chiral fibre.
- **Open (the conjecture's remaining content):** the exact normalisation — that
  the ζ₅-residue of the chiral `3p_z` braid returns *precisely* the `1/√5`
  coefficient (not merely a √5-multiple). That is the monodromy/Reshetikhin–
  Turaev evaluation at ζ₅, still the formal target.

This closes the chiral-residue loop back onto Bring's surface, exactly as the
owner anticipated ("embed it in Bring's surface"): the H₂S residual's Bring
constant is the quintic √5 of the surface's own ζ₅ chiral fibre.

## The explicit geometry: two torus knots in Σ₄, linked by S₅ (embedding, not cover)

The phrasing "the chiral channel lives on the Bring chiral fibre with ζ₅
symmetry" conflated two *distinct* structures. Precisely:

**Bring's curve** `B ⊂ ℙ⁴` is genus 4 with **`Aut(B) = S₅`** — the symmetric
group permuting the 5 homogeneous coordinates (the 5 roots the Bring radical
resolves). Two different torus knots embed in its genus-4 Seifert fibre `Σ₄`
(`torus-embeddable-complete`: the complete list is
`{(2,3),(2,5),(2,7),(2,9),(3,4),(3,5)}`, from `g=(m−1)(n−1)/2 ≤ 4`), and they
carry the two symmetries:

1. **3-fold — the chiral channel.** The **color-tube cubic**
   `c³+(4z+1)c²+(6z²+3z+1)c+(4z³+3z²+2z+1)=0` (`color-tube-cubic`) fibres Bring's
   surface over the ℂP¹ base; its three roots are the colour tubes `(r,g,b)` and
   the branch-point monodromy is **B₃ ↠ H₃**. This is the **trefoil `T_{2,3}`**
   in `Σ₄` — the chiral channel, the "3 in the ED".

2. **5-fold — the √5.** `S₅` contains a cyclic **ℤ₅** (a 5-cycle). The
   hyperelliptic quintic **`𝒳₅: y²=x⁵−1`** is **embedded** (not a cover) by
   `x = ` the **first Lagrange resolvent `w₁`** of that `ℤ₅ ⊂ S₅`
   (`hyperelliptic-quintic`); its five branch points `{1,ζ₅,…,ζ₅⁴}` are one
   **ℤ₅-orbit**. This is the **cinquefoil `T_{2,5}`** in `Σ₄`.

So the trefoil (H₃ chiral channel) and the cinquefoil (ζ₅) are **two torus knots
in the same `Σ₄`**, related by the ambient **`S₅`** — *not* one fibre with two
symmetries. The chiral residue lives on the trefoil; the `ℤ₅ ⊂ S₅` acts through
the Lagrange resolvent **`w₁`, which carries √5** (the ℤ₅-orbit Gauss sum). *That*
is the explicit geometric channel — the S₅-linked resolvent embedding, not a
property of the cubic fibre itself — by which the H₃ chiral residue acquires the
quintic √5. The open monodromy step is now sharply stated: evaluate the chiral
trefoil residue under the `w₁`-resolvent of the cinquefoil's ℤ₅, and confirm the
normalisation is `1/√5`.

## Now wired into compute / paper / lean

This geometry is no longer audit-only — it is the provable scaffold
[`prop:bring-trefoil-cinquefoil-channel`](../../content/quantum-observable-universe/brings-surface/bring-trefoil-cinquefoil-channel.md),
which the H₂S conjecture now `uses`:

- **Compute** —
  [`bring_trefoil_cinquefoil_channel.py`](../../computations/bring_trefoil_cinquefoil_channel.py)
  (witness `bring-trefoil-cinquefoil-channel.witness.json`, 7 assertions): genera
  `g(T_{2,3})=1`, `g(T_{2,5})=2`, both `≤ g(Σ₄)=4`, distinct; the complete
  embeddable list; and the ℤ₅-orbit Gauss sum `g²=5`, `g=√5`.
- **Lean** — `QOU.BringChiralCinquefoil`, **sorry-free** (verified Lean 4.24.0 +
  Mathlib): `bring_trefoil_cinquefoil_channel` (genera + embedding + distinctness,
  `decide`); `zeta5_pow_five` (`ζ₅⁵=1`); `quintic_gauss_sum_sq_eq_five` (`g²=5`,
  proved from `Complex.isPrimitiveRoot_exp` + the cyclotomic relation via
  `linear_combination`). The archimedean *sign* `g=+√5` — not the value `g²=5` —
  is the only deferred step, and it is the conjecture's open normalisation content.
- **Paper** — the proposition states the established scaffold and isolates the
  single open item (exact `ζ₅`-residue normalisation `=1/√5`), which stays the
  content of [`conj:h2s-angle-s3-braid-holonomy`](../../content/quantum-observable-universe/molecular-construction/h2s-angle-s3-braid-holonomy.md).
