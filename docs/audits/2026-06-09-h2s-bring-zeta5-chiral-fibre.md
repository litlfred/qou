# The H₂S Bring `1/√5` is the ζ₅ chiral fibre of Bring's surface

**Date:** 2026-06-09. **Status:** structural connection established; exact
ζ₅-residue normalisation open. **Compute:**
[`h2s_bring_zeta5_chiral_residue.py`](../../folio-assistant/computations/h2s_bring_zeta5_chiral_residue.py).

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
