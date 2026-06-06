# VolDensity derivation: step-by-step from categorical action to the geometric gap

## Where we are in the pipeline

The QOU mass formula descends through four layers. VolDensity is where
the **algebraic** layer meets the **geometric** layer — the point where
abstract Hecke-algebra identities must be evaluated on a specific
knot/braid, and the knot's topology enters.

---

## Step 1: Categorical action (Cat layer)

**Definition.** The categorical action is a braided monoidal functor

    ρ_n : B_n → Aut_𝐂(V^{⊗n})

from the braid group B_n to automorphisms of the n-fold tensor product
of the fundamental object V in a ribbon category 𝐂.

This is the R-matrix representation: each braid generator σ_i acts on
strands i and i+1 via the R-matrix R ∈ End(V ⊗ V).

**No geometry here.** The categorical action is abstract — it doesn't
know about specific knots, masses, or MeV.

---

## Step 2: Hecke quotient (Cat → Alg transition)

**The Yekutieli non-abelian Stokes argument** shows that the curvature
2-form of the categorical connection satisfies the Hecke relation:

    σ_i² = (q − q⁻¹)σ_i + 1

This quotients the braid group algebra ℂ[B_n] to the Iwahori–Hecke
algebra H_n(q). The deformation parameter q is ABSTRACT here — not
yet the substrate value q₀.

**The Wedderburn decomposition** (Artin–Wedderburn theorem):

    H_n(q) ≅ ⊕_{λ ⊢ n} M_{d_λ}(k)

Each partition λ ⊢ n gives an irreducible representation V_λ with
quantum dimension d_λ(q). The three blocks for n = 3 are:
- sym: λ = (3), d = 1, eigenvalue +q
- std: λ = (2,1), d = 2, eigenvalues +q and −q⁻¹
- alt: λ = (1,1,1), d = 1, eigenvalue −q⁻¹

---

## Step 3: Markov trace (Alg layer)

**The Markov trace** tr_M is the unique trace on H_n(q) satisfying
the Markov property (invariance under braid stabilization). It
decomposes via the Wedderburn blocks:

    tr_M(x) = Σ_λ y_λ · χ^λ(x)

where:
- y_λ = Markov weight (from Wenzl's formula, algebraic in q)
- χ^λ(x) = character of x in V_λ (trace of the representation matrix)

**Still no geometry.** Everything is algebraic in the generators σ_i
and the parameter q.

---

## Step 4: Braid word evaluation (Alg → Geom transition)

**Here geometry enters.** To get a mass, we evaluate χ^λ on a SPECIFIC
braid word β_K:

    χ^λ(β_K)

The braid word β_K encodes the topology of knot/particle K. For:
- electron: β = σ₁³ (trefoil, 3 crossings)
- proton: β = (σ₁σ₂⁻¹)³ (Borromean, 6 crossings)
- deuteron: β = β_p ⊗ I ⊗ β_n (proton + interface + neutron, 23 crossings)

The character χ^λ(β_K) is computed via the **Hoefsmit seminormal form**:
each σ_i acts as a d_λ × d_λ matrix, and β_K is a product of ~20
such matrices. The result is a NUMBER (at specific q).

**The interface operator** σ_{3i} (connecting nucleon i and i+1 within
H_{3A}) is what makes composite atoms different from free nucleon
products. It's a GEOMETRIC operator — it depends on the specific
braid topology of the bound state.

---

## Step 5: Mass formula (Geom layer)

The mass of particle K is:

    m(K) = m_e × VolDensity(K, q₀)

where VolDensity is the "geometric evaluation" that combines the
Markov trace with the knot's topology.

**For knots (single-component, like the electron):**

    VolDensity(K) = Vol_hyp(K) / ℏ_q²

where Vol_hyp is the hyperbolic volume of the knot complement.
No linking weight needed (linking weight = 1 for knots).

**For links (multi-component, like the proton = Borromean link):**

    VolDensity(K) = Vol_hyp(K) / ℏ_q² × linking_weight(q)

The linking_weight accounts for the multi-component topology.
For the proton (Borromean link B₃):

    linking_weight_A(q) = (3q² + 4 + 3q⁻²)/4

This is PROVED (Lean + Python) and comes from the Wedderburn
decomposition of H_4 — the "next" Hecke algebra.

**THE GAP IS HERE.** The linking_weight formula is proved for the
proton (H_3 → H_4 transition). For BINDING energies of composite
atoms (deuteron at H_6, tritium at H_9, etc.), the analogous
linking weight at the H_{3A} → H_{3A+1} transition is NOT derived.

---

## Step 6: Archimedean evaluation (Geom → Arch)

Substitute q = q₀ ≈ 1.1100 (from CAL-2: m_μ/m_e = Vol(4₁)/ℏ_q²):

    m(K) = m_e × VolDensity(K, q₀) |_{q = q₀}

All q-dependent expressions become numbers in ℝ.

---

## Where VolDensity appears in binding

For the binding energy B(K) of a composite atom K:

    B(K) = m_e × Σ_λ y_λ(q₀) · χ^λ(β_K, q₀) · Δ_λ

We proved (this session): Δ_λ = sgn(w_0^{S_{λ'}}) × f^λ

The ABSOLUTE binding is then:

    B(K) = m_e × |Σ_λ y_λ · χ^λ(β_K) · sgn · f^λ| × linking_weight_binding(K)

The last factor — linking_weight_binding(K) — is what's missing.
It's the per-knot geometric correction from the Geom layer, analogous
to the proton's (3q²+4+3q⁻²)/4 but for the atom's specific braid
topology.

---

## What we know about the gap

| Atom | B_pred (without lw) | B_AME | Scale needed |
|------|-------------------|-------|-------------|
| D    | 0.38 MeV         | 2.22  | 5.85×       |
| T    | 1.91 MeV         | 8.48  | 4.44×       |
| ³He  | 2.34 MeV         | 7.72  | 3.29×       |
| ⁴He  | 3.04 MeV         | 28.3  | 9.31×       |

The scale factor varies per knot (2.8× spread). It's the same
structural gap as the proton mass (2.89% = linking_weight imprecision).

**Closing it = deriving linking_weight_binding(K) from the Wedderburn
structure of H_{3A+1}, the way lw_A was derived from H_4.**
