# Phase 3 — Atom-knot derivation: corrected analysis

*Companion to `docs/path-to-1ppb-04-plan.md` Phase 3. Records the
initial attempt to compute an atom's volume via SnapPy on its braid
closure, and why that approach was misframed.*

**Status.** The "block vs interleaved lift" framing in the earlier
draft of this doc was wrong. The atom's braid word is
**topological data**, not a derived invariant. The question "which
lift is canonical?" does not arise — `atom_braid_word_3A` outputs the
atom's braid word directly, and that IS the data. What's wrong is
asking SnapPy for its hyperbolic volume.

## The correct invariant

The paper's definition `def:algebraic-quantum-volume`
([`content/quantum-observable-universe/braids-and-knots/algebraic-quantum-volume.md`](../content/quantum-observable-universe/braids-and-knots/algebraic-quantum-volume.md))
gives the algebraic quantum volume of a braid $\beta \in H_n(q)$ as

$$
  \mathrm{Vol}_q(\beta)
  = \prod_{i=0}^{n-2} \hat{V}_i(q),
  \qquad
  \hat{V}_i(q) = z(q) \cdot a_i(q) + b_i(q)
$$

where $\hat{V}_i$ comes from the transfer-matrix chain of the Markov
trace. This is a finite product of Laurent polynomials in
$q^{1/2}$; it lives in the Habiro ring
$\widehat{\mathbb{Z}[q^{1/2}]}$; it is **algorithmic** from the
Hecke element.

The paper's binding formula (`def:algebraic-quantum-volume-specialization`)
is the substrate evaluation:

$$
  \Phi_1(\beta) = \ln\bigl\lvert\mathrm{Vol}_{q_0}(\beta)\bigr\rvert
  = \sum_{i=0}^{n-2} \ln\bigl\lvert\hat{V}_i(q_0)\bigr\rvert
$$

$$
  \mathcal{M}(Z, N)
  = M_{\text{free}}
  + \bigl(m_e \cdot 8G\bigr) \cdot \Phi_1(\text{atom}) \cdot \text{(Wedderburn weights)}
$$

The key invariant is $\Phi_1$ as a complex number at $q_0$, NOT
$\mathrm{Vol}_{\text{hyp}}(\widehat{\beta})$ from SnapPy.

## Why SnapPy was the wrong tool at $q_0$

SnapPy computes the hyperbolic volume of the 3-manifold
$S^3 \setminus \widehat{\beta}$, which is a **topological invariant**
of the link class. The algebraic volume $\mathrm{Vol}_{q_0}(\beta)$
is an **algebraic invariant** of the Hecke element, parametrised by
$q_0$. These two coincide only via the volume-conjecture asymptotic
at **roots of unity** $q = e^{2\pi i/N}$ (Kashaev–Murakami–Murakami):

$$
  \lvert J_N(K;\, e^{2\pi i/N})\rvert
  \sim \exp\bigl(N \cdot \mathrm{Vol}_{\text{hyp}}(S^3 \setminus K) / 2\pi\bigr)
$$

At $q_0 \approx 1.10998$ (real, not a root of unity) the asymptotic
does not apply. The quantity that enters the mass formula is the
direct evaluation $\mathrm{Vol}_{q_0}(\beta) = \prod \hat{V}_i(q_0)$.

## Practical consequence

The canonical 1-ppb pipeline does **not** need SnapPy as a primary
invariant engine. The primary engine is:

1. `atom_braid_word_3A` → braid word as a list of Hecke factors
   (block form: `σ_0^a · σ_1^b · …`). This IS the atom's data.
2. Transfer-matrix chain in $\mathbb{Z}[q^{1/2}, q^{-1/2}]$ → per-gen
   $\hat{V}_i(q)$. See `computations/exact_binding_per_operation.py`
   (method `compute_phi_mp`) for a working mpmath-precision implementation.
3. Evaluate at $q_0$, take $\ln|\cdot|$, sum → $\Phi_1$.
4. Apply $\mathcal{M} = M_{\text{free}} + \alpha \cdot \Phi_1 \cdot (\text{Wedderburn})$.

SnapPy enters only at **step zero**, to witness the 8G scale factor
via route 2 (Habiro / colored Jones at roots of unity). The value
$8G = \mathrm{Vol}(\mathcal{B}_3) = 7.327725\ldots$ is a fixed
constant; it does not need to be recomputed per atom.

## What `atom_link_derivation.py` is, and is not

The prototype at
`computations/atom_link_derivation.py`
closes the braid word and hands it to SnapPy. This is useful for
diagnostic purposes — it lets us see what link class the braid
closes to, and confirms (via block closure → non-hyperbolic) that
the current `atom_braid_word_3A` output is a braid word representing
a satellite/torus link, not the Borromean rings.

But this does **not** give the atom's binding energy. It answers a
different question: "what is the topology of the braid closure?"
The answer happens to be "non-hyperbolic", which is fine — the
binding formula does not depend on hyperbolicity.

## The `jsj_atom_volume.py` discrepancy

`computations/jsj_atom_volume.py` uses the
Borromean-rings model `B = 2m_e · A · 8G` (one Borromean per
nucleon). This implicitly assumes the atom braid IS
$(\sigma_0 \sigma_1^{-1})^3$ per nucleon — a different model from
`atom_braid_word_3A`'s block form.

These two models produce:

- Same Hecke element → same $\Phi_1$ → same $\mathcal{M}$
- Different link class → different hyperbolic volume

The mass formula depends only on $\Phi_1$, so both models give the
same mass prediction. The apparent tension (block closure has
Vol = 0, `jsj_atom_volume` claims Vol = $A \cdot 8G$) dissolves
because only one of those volumes appears in the formula: neither,
directly. What appears is $\Phi_1$, which is model-independent.

The `A · 8G` heuristic in `jsj_atom_volume.py` is a **rescaling
convenience**, not a computation of Vol. It uses $8G$ as the
energy-per-nucleon scale, which follows from route 2 (Habiro
evaluation) but does not require computing a per-atom hyperbolic
volume.

## Action items

- **Done:** Document the correct framing (this file).
- **Fix:** Drop any narrative in the main plan suggesting that
  hyperbolic volume of the braid closure is the per-atom invariant.
- **Next:** Produce a mass table directly from $\Phi_1$ via the
  algebraic volume pipeline, evaluated at 100-digit mpmath precision
  at $q_0$, applying the full Wedderburn-weighted formula from
  `def:algebraic-quantum-volume-specialization`. See
  `computations/mass_table_ppb.py`.
