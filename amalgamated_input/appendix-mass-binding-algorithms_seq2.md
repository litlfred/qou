<!-- FILE_START: mba-step01-categorical-action.md -->
**Algorithm (Categorical action of the braid group).**
*Construct the representation
$\rho_n\colon B_n \to \mathrm{Aut}_{\mathbf{C}}(V^{\otimes n})$
that sends each braid generator $\sigma_i$ to a categorical
endomorphism of the $n$-fold monoidal product
$V^{\otimes n}$ in $\mathbf{C}$.*

### Input

- *Braid word $w = \sigma_{i_1}^{\varepsilon_1} \cdots \sigma_{i_k}^{\varepsilon_k}$ in $B_n$.*
- *Underlying rigid monoidal category $\mathbf{C}$ with chosen
  generating object $V \in \mathbf{C}$.*

### Output

- *Endomorphism $\rho_n(w) \in \mathrm{Aut}_{\mathbf{C}}(V^{\otimes n})$
  as a finite composition of categorical generators
  (braiding $c_{V,V}$, dualities $\mathrm{ev}_V$, $\mathrm{coev}_V$,
  associator, unit).*

### Algorithm

```
1. For each generator σ_i in w:
     interpret σ_i as id^{i-1} ⊗ c_{V,V} ⊗ id^{n-i-1}
     where c_{V,V} is the braiding of C at (V, V).
2. For σ_i^{-1}: use c_{V,V}^{-1} = c_{V,V}^* (left-rigid dual).
3. Compose in order along w; the result is ρ_n(w).
```

### Correctness conditions

*Correctness rests on three upstream results.*

1. *The categorical action is **well-defined** by
   [`def:categorical-action`](#def:categorical-action) — the
   braiding $c_{V,V}$ in a rigid monoidal category satisfies the
   braid (Yang–Baxter) relations on $V^{\otimes n}$ by naturality
   of the hexagon axioms.*
2. *It **exists** under the QOU rigid-monoidal premise by
   [`prop:categorical-action-exists`](#prop:categorical-action-exists).*
3. *It is **unique** up to natural isomorphism by
   [`prop:categorical-action-unique`](#prop:categorical-action-unique).*

### Complexity

*$O(k)$ categorical morphisms for $|w| = k$. The endomorphism is
stored implicitly as a braid word until passed to the next step
(GS reduction), so the representation is **lazy** — no matrix
exponentiation occurs at this layer.*

### Python / Rust API entry point

*No standalone Python entry point — the categorical action is the
upstream specification, realised implicitly inside the Rust
`hecke-engine` crate at [`tools/hecke-engine/src/lib.rs`](../../../tools/hecke-engine/src/lib.rs).
Per-particle braid words are constructed via
`pyhecke.build_nucleon_nf` / `pyhecke.build_atom_nf` and consumed
by Step 2 (GS reduction).*

### Witness contract

*No standalone witness JSON: correctness is checked structurally
(braid relations are obeyed by the Hecke-relation specialisation
in Step 2). Property tests live in `tools/hecke-engine/tests/`.*

### Notes

*The categorical action is **fibre-independent**: it depends only
on the rigid-monoidal structure of $\mathbf{C}$, not on the choice
of fibre functor $\tau$. The archimedean specialisation enters at
Step 9 (mass identity) via the Markov trace evaluation at $q_0$.*
<!-- FILE_END: mba-step01-categorical-action.md -->

<!-- FILE_START: mba-step02-gs-reduction.md -->
**Algorithm (Gröbner–Shirshov reduction to Hecke normal form).**
*Quotient a braid-word $w \in B_n$ by the Hecke relation
$\sigma_i^2 = (q - q^{-1})\sigma_i + 1$ to produce its canonical
representative $\mathrm{NF}(w) \in H_n(q)$.*

### Input

- *Braid word $w \in B_n$ (output of Step 1 / `alg:categorical-action`).*
- *Substrate parameter $q \in R$ (symbolic or pinned to $q_0$).*

### Output

- *Hecke normal form $\mathrm{NF}(w) = \sum_{i} c_i(q)\, T_{w_i}$ as
  an $R$-linear combination of basis elements $T_{w_i}$ indexed by
  permutations $w_i \in S_n$ (the standard $H_n(q)$ basis), with
  coefficients $c_i(q) \in R[q, q^{-1}]$.*

### Algorithm

```
1. Initialize NF ← w (read as a formal product of σ_i^{±1}).
2. Repeat until no rewrite rule applies:
   a. Apply braid relations σ_iσ_jσ_i = σ_jσ_iσ_j (|i-j| = 1)
      to canonicalise commuting / braided pairs.
   b. Apply the Hecke relation σ_i² = (q - q^{-1})σ_i + 1
      to eliminate self-squares, generating two summands.
   c. For σ_i^{-1}: rewrite σ_i^{-1} = σ_i − (q − q^{-1}) using
      the same Hecke quotient.
3. Collect like terms; output as Σ c_i(q) · T_{w_i}.
```

### Correctness conditions

*Correctness rests on two upstream definitions.*

1. *[`def:hecke-normal-form`](#def:hecke-normal-form) defines
   $H_n(q)$ as the quotient of the group algebra $R[B_n]$ by the
   Hecke ideal $\langle \sigma_i^2 - (q-q^{-1})\sigma_i - 1 \rangle$.
   The standard $T_w$ basis is then well-defined.*
2. *[`def:categorical-action`](#def:categorical-action) ensures
   that the braiding $c_{V,V}$ in $\mathbf{C}$ obeys the Hecke
   relation (the categorical specialisation that makes $\rho_n$
   factor through $H_n(q)$).*

*Confluence of the rewriter is structural: any two reduction
orders end at the same normal form by the Diamond Lemma applied
to the Hecke and braid relations (both are linear quadratic and
mutually compatible).*

### Complexity

*Worst case: exponential in $n$ (the partition count for $H_n(q)$).
Polynomial in $|w|$ after caching cycle-equivalent words. For
nucleon-scale knots ($n \leq 9$, $|w| \leq 24$) the reducer
finishes in milliseconds on the Rust core.*

### Python / Rust API entry point

```python
# Per-particle Hecke normal forms (the user-facing surface):
from pyhecke import (
    build_nucleon_nf, build_atom_nf, build_atom_nf_exact,
)

nf_proton  = build_nucleon_nf("proton")
nf_atom    = build_atom_nf(Z=2, N=2)        # ⁴He
nf_exact   = build_atom_nf_exact(Z=2, N=2)  # symbolic
```

*The Rust core is at [`tools/hecke-engine/src/gb_nf_reducer.rs`](../../../tools/hecke-engine/src/gb_nf_reducer.rs)
(canonical implementation, called via the `pyhecke-native` PyO3
wheel from the builders above).*

### Witness contract

*Canonical witness:
[`hecke-core-symbolic-migration.witness.json`](../../../computations/hecke-core-symbolic-migration.witness.json).
Records the input braid, the output basis-decomposition vector,
the chosen $q$ evaluation, and a hash of the rewriter source for
reproducibility. Per-particle assemblies are captured in
`markov-trace-assembly-{proton,neutron,deuteron}.derivation.json`
(consumed by Step 3).*

### Notes

*The reducer is the **single source** of Hecke normal forms in the
QOU pipeline; every downstream algorithm consumes `NF(w)`, not the
raw braid word. Treating the normal form as the canonical object
(rather than the braid) is what makes the rest of the chain
$q$-rational.*
<!-- FILE_END: mba-step02-gs-reduction.md -->

<!-- FILE_START: mba-step03-markov-trace.md -->
**Algorithm (Markov trace on $H_n(q)$).**
*Compute the categorical observation
$\mathrm{tr}_M\colon H_n(q) \to R[q, q^{-1}]$ of a braid word
$w \in B_n$ in Hecke normal form.*

### Input

- *Braid word $w = \sigma_{i_1}^{\varepsilon_1} \cdots \sigma_{i_k}^{\varepsilon_k}$ in
  $B_n$ (the closure of $w$ is the knot or link whose mass we
  predict).*
- *Substrate parameter $q \in R$ — either symbolic
  (for an algebraic identity) or pinned to $q_0$
  for a numerical evaluation.*

### Output

- *The Markov trace
  $\mathrm{tr}_M(\rho(w)) \in R[q, q^{-1}]$ as a Laurent polynomial
  (symbolic mode) or as an arbitrary-precision scalar evaluation at
  $q = q_0$ (numerical mode).*

### Algorithm

```
1. Reduce w to its Hecke normal form NF(w) via the
   Gröbner–Shirshov rewriter (Algorithm 2).
2. Decompose NF(w) along the Wedderburn isotypic components
   H_n(q) ≅ ⊕_{λ ⊢ n} M_{d_λ}(R) (Algorithm 5).
3. For each partition λ ⊢ n with multiplicity y_λ(q), evaluate the
   irreducible character χ^λ(σ_w) on the Hoefsmit representation.
4. Return the Frobenius pairing tr_M(σ_w) = Σ_λ y_λ(q) · χ^λ(σ_w).
```

### Correctness conditions

*Correctness follows from three upstream results.*

1. *Existence and uniqueness of the trace is established by the
   axiomatic closed form
   ([`prop:markov-trace-axiomatic-closed-form`](#prop:markov-trace-axiomatic-closed-form)):
   $\mathrm{tr}_M$ is the unique $R$-linear functional on $H_n(q)$
   satisfying (i) cyclicity, (ii) the Markov axiom
   $\mathrm{tr}_M(a\sigma_n) = z \cdot \mathrm{tr}_M(a)$ for
   $a \in H_n(q)$, and (iii) normalisation
   $\mathrm{tr}_M(1) = 1$.*
2. *The recursive-reducer formula
   ([`prop:markov-trace-recursive-reducer`](#prop:markov-trace-recursive-reducer))
   gives a terminating reduction strategy by descent on braid index,
   so step 1 always terminates.*
3. *The Frobenius pairing in step 4 is justified by the Wedderburn
   decomposition; cyclicity makes the trace partition-respecting,
   so the sum is well-defined and independent of the chosen
   representative within each conjugacy class.*

### Complexity

*Polynomial in the braid index $n$ and the word length $|w|$ in
the symbolic regime. The dominant cost is the GS reduction in
step 1 (worst case exponential in $n$, polynomial in $|w|$ after
caching cycle-equivalent words). The Wedderburn sum in step 4 has
$|\{\lambda \vdash n\}|$ terms — for nucleon-scale knots
($n \leq 9$) the partition count is at most 30.*

### Python API entry point

```python
from qou_mass import compute_tr_M, canonical_braid

word = canonical_braid(Z=1, N=0)              # proton braid 𝓑₃
trM  = compute_tr_M(Z=1, N=0)                 # Decimal at q = q_0
```

*The lower-level `pyhecke` surface exposes the trace on a Hecke
normal form: `pyhecke.nf_tr(nf)`. The compile-time Markov-trace
vector for the 6-element basis is the constant `pyhecke.TR_M`.
The PyO3 binding `pyhecke_native` calls the Rust core directly.*

### Witness contract

*Canonical witness:
[`markov-free-energy-qvalues.witness.json`](../../../computations/markov-free-energy-qvalues.witness.json).
Per-particle assembly traces are emitted separately as
`markov-trace-assembly-{proton,neutron,deuteron}.derivation.json`.
Each witness records the input braid word, the chosen $q$
evaluation, the resulting Laurent polynomial (symbolic mode) or
mpmath scalar (numerical mode, default 65 dps compute /
50 dps serialisation), and a SHA-256 digest of the canonical
script source for reproducibility.*

### Notes

*Precision regime: the symbolic mode is exact (L1 met
trivially). The numerical mode at $q = q_0$ meets L1 to
$10^{-50}$ by the precision discipline of `qou-substrate`. The
per-observable L2 target inherits the calibration floor of the
downstream mass identity (step 9a).*

*Edge cases: the identity braid $1 \in B_n$ has
$\mathrm{tr}_M(1) = 1$; closure of any braid containing a full
twist $\Delta_n^2$ in the centre acquires a factor
$(q^{n(n-1)})$ from the central character (Schur–Weyl).*

*Large-$A$ scaling (atom braids of step 9b): the multi-nucleon
braid word has a **monotone** non-decreasing generator sequence —
nucleon $k$ uses $\sigma_{3k},\sigma_{3k+1}$ and one interface
crossing $\sigma_{3k+2}$, never revisiting a generator — so each
$O_g$ is a polynomial in a single $\sigma_g$. In the
multiplicity-free seminormal (Gelfand–Zetlin) basis $\sigma_g$
moves only one level of the chain
$\varnothing \subset s_1 \subset \cdots \subset s_n = \lambda$, and
trace closure forces each $O_g$ to its diagonal block, collapsing
step 3–4 to a transfer matrix over fine-Bratteli edges
$s_g \subset s_{g+1}$. This yields every $\chi^\lambda(\beta)$ in a
single sweep without materialising the $d_\lambda$-dimensional
Hoefsmit representation: the cost is the fine-Bratteli edge count
(a few thousand at $n = 21$) rather than $n!$, extending the
numerical $\mathrm{tr}_M$ at $q_0$ to $A \geq 6$ ($^6$Li, $^7$Li,
and beyond) in seconds. Implemented in
[`chi_monotone_transfer.py`](../../../computations/chi_monotone_transfer.py)
with the per-atom trace assembly in
[`tr_m_atom_via_transfer.py`](../../../computations/tr_m_atom_via_transfer.py)
(witness
[`tr-m-atom-via-transfer.witness.json`](../../../computations/tr-m-atom-via-transfer.witness.json)),
validated to the 50-dps floor against the Hoefsmit characters
($n \leq 6$) and the cached per-basis-vector trace witnesses
($n \leq 12$). The production binding consumers
[`binding_canonical`](../../../computations/binding_canonical.py)
and
[`canonical_tr_m_via_branching`](../../../computations/canonical_tr_m_via_branching.py)
($A \geq 3$) route their atom-trace through this transfer path (the
former brute-force atom-level Wedderburn tower,
`atom_level_wedderburn_tower.py`, is retained only as a
$d_\lambda$-explicit cross-check).*
<!-- FILE_END: mba-step03-markov-trace.md -->

<!-- FILE_START: mba-step04-bring-brane.md -->
**Algorithm (Bring brane constants).**
*Return the substrate constants of the
Bring surface $\mathcal{E}_q$ (Euler characteristic $\chi = -6$,
six torus-knot embeddings, fundamental-group presentation) used by
every downstream step.*

### Input

- *(none — the Bring brane is a fixed geometric object).*

### Output

- *Tuple $(\chi, g, k, \mathrm{Aut})$ with $\chi = -6$, genus
  $g = 4$, $k = 6$ torus-knot embeddings $T_{p_i, q_i}$, and
  $\mathrm{Aut}(\mathcal{E}_q) = S_5$.*

### Algorithm

```
1. Return χ = -6, g = 4.
2. Return the six embeddings T_{p_i, q_i} for i = 1, …, 6.
3. Return Aut group S_5 (the small simple group acting on
   Bring's coordinate ring).
```

### Correctness conditions

*Settled by [`def:brings-surface`](#def:brings-surface): the
Bring surface is uniquely characterised (up to isomorphism) by
its Euler characteristic and the six-fold $S_5$-symmetric
embedding. No upstream calibration; the values are categorical
constants.*

### Complexity

*$O(1)$ — table lookup.*

### Python API entry point

*The Bring constants are produced by the canonical script
[`computations/bring_chiral_fibre_figure.py`](../../../computations/bring_chiral_fibre_figure.py),
which emits the witness JSON consumed by every downstream step.
The substrate parameter $q_0$ and its derived constants live in
[`qou_substrate.constants`](../../../tools/qou-substrate/python/qou_substrate/constants.py).*

### Witness contract

*Canonical witness:
[`bring-chiral-fibre-figure.witness.json`](../../../computations/bring-chiral-fibre-figure.witness.json).
Records the six torus-knot embeddings, their chirality, and the
$S_5$ action.*

### Notes

*The Bring brane is **not** a calibration input — it is a
mathematical constant fixed by the rigid-monoidal premise. The
choice of $\chi = -6$ is what gives the substrate its
6-knot decomposition and ultimately the torsion structure that
feeds Step 7 (GB filtration).*
<!-- FILE_END: mba-step04-bring-brane.md -->

<!-- FILE_START: mba-step05-wedderburn.md -->
**Algorithm (Wedderburn decomposition of $H_n(q)$).**
*Decompose the Hecke algebra into its isotypic components indexed
by partitions $\lambda \vdash n$, yielding the Frobenius pairing
$\mathrm{tr}_M = \sum_\lambda y_\lambda(q)\, \chi^\lambda$ used by
Step 3.*

### Input

- *Braid index $n \in \mathbb{N}_{\geq 1}$ and substrate
  parameter $q \in R$.*

### Output

- *List of pairs $\{(\lambda, d_\lambda, y_\lambda(q))\}_{\lambda \vdash n}$
  where $d_\lambda = \dim_R V^\lambda$ (Hoefsmit-block dimension)
  and $y_\lambda(q)$ is the Wenzl–Markov $q$-weight.*

### Algorithm

```
1. Enumerate partitions λ ⊢ n.
2. For each λ:
   a. Compute d_λ (Frobenius hook-length formula at q = 1, then
      q-deform via [hook]_q).
   b. Compute y_λ(q) via the Wenzl bridge
      (`prop:wenzl-bridge-applicability-qou`).
   c. Cache the Hoefsmit irrep ρ^λ on H_n(q).
3. Return the decomposition.
```

### Correctness conditions

1. *[`prop:wedderburn-trace-identity`](#prop:wedderburn-trace-identity)
   gives the canonical sum $\mathrm{tr}_M = \sum_\lambda y_\lambda\,\chi^\lambda$.*
2. *[`prop:wenzl-bridge-applicability-qou`](#prop:wenzl-bridge-applicability-qou)
   asserts that the Wenzl bridge applies in the QOU setting,
   giving a closed-form recursion for $y_\lambda(q)$.*
3. *[`prop:wedderburn-as-noncomm-fourier`](#prop:wedderburn-as-noncomm-fourier)
   establishes the algebra-level isomorphism as a non-commutative
   Fourier transform.*

### Complexity

*$O(p(n))$ partitions, each requiring $O(n^2)$ hook-length / cell
products. For $n \leq 9$ (nucleon-scale): at most 30 partitions.*

### Python API entry point

```python
from pyhecke import wedderburn_weight, partitions_of, partition_dimension

for lam in partitions_of(n):
    y_lam = wedderburn_weight(lam, q)
    d_lam = partition_dimension(lam)
```

*The per-partition heavy lifting lives in the submodule
[`pyhecke.wedderburn`](../../../tools/pyhecke/python/pyhecke/wedderburn.py).*

### Witness contract

*Canonical witness:
[`wedderburn-lp-ew-wiring.witness.json`](../../../computations/wedderburn-lp-ew-wiring.witness.json).
Records the per-partition $(d_\lambda, y_\lambda(q))$ table, the
chosen $q$, and the upstream Hoefsmit cell-content table from
`prop:hoefsmit-ew-cell-content` for cross-checking.*

### Notes

*The Wedderburn decomposition is the **single most expensive
step** in the chain for $n > 6$ because $y_\lambda(q)$ involves
nested $[k]_q$ factors. The native Rust core caches partitions
across braid-trace calls.*
<!-- FILE_END: mba-step05-wedderburn.md -->

<!-- FILE_START: mba-step06-frobenius-pairing.md -->
**Algorithm (Frobenius pairing + self-duality check).**
*Compute the symmetric bilinear pairing
$\langle a, b\rangle_F = \mathrm{tr}_M(a \cdot b)$ on $H_n(q)$ and
verify the categorical self-duality $\Psi = S^2 = \mathrm{id}$
(dualities D3 and D23 in the canonical-derivation tracker).*

### Input

- *Two Hecke normal forms $a, b \in H_n(q)$ (output of Step 2).*
- *Substrate parameter $q \in R$.*

### Output

- *Scalar $\langle a, b\rangle_F \in R[q, q^{-1}]$.*
- *Boolean assertion that $S^2 = \mathrm{id}$ holds on $a$ (and on
  every basis $T_w$).*

### Algorithm

```
1. Compute the product a · b in H_n(q) via GS reduction (Step 2).
2. Apply tr_M to the product (Step 3).
3. Optional: verify self-duality by computing S(a) and S(S(a))
   on each basis element T_w; assert S²(T_w) = T_w.
```

### Correctness conditions

1. *[`def:frobenius-pairing`](#def:frobenius-pairing) defines
   $\langle a, b\rangle_F$ as the Markov trace of the product,
   making it symmetric and non-degenerate.*
2. *[`prop:frobenius-pairing-exists`](#prop:frobenius-pairing-exists)
   gives existence in the QOU rigid-monoidal premise.*
3. *[`prop:frobenius-pairing-unique`](#prop:frobenius-pairing-unique)
   makes the pairing canonical (up to the chosen Markov parameter).*

### Complexity

*$O(\dim H_n(q))$ products + a single trace; dominated by
Step 2 (GS reduction). The $S^2 = \mathrm{id}$ check is
$O(\dim H_n(q))$ basis-element verifications.*

### Python API entry point

```python
from pyhecke import check_frobenius

# Verifies Frobenius positivity Gx ≥ 0 on the standard basis vector x.
ok = check_frobenius(x)
```

*The canonical audit script is
[`computations/audit_frobenius_pairing.py`](../../../computations/audit_frobenius_pairing.py);
the Gram matrix `G` and the Markov-trace vector `TR_M` are
exposed as constants by `pyhecke`.*

### Witness contract

*No standalone numerical witness file. Structural checks live in
`computations/audit_frobenius_pairing.py`; the
$S^2 = \mathrm{id}$ assertion is part of the Hecke-core
regression suite.*

### Notes

*The Frobenius pairing is what makes $H_n(q)$ a **rigid**
Frobenius algebra — the categorical self-duality is dual to it
under decategorification. Both are required for the Wedderburn
decomposition (Step 5) to land in the correct basis.*
<!-- FILE_END: mba-step06-frobenius-pairing.md -->

<!-- FILE_START: mba-step07-gb-filtration.md -->
**Algorithm (Gröbner–Shirshov filtration with $E_2$ collapse).**
*Compute the length-graded filtration on $H_n(q)$ and assert
$E_2$-collapse of the associated spectral sequence — every higher
differential $d_r$ ($r \geq 2$) vanishes.*

### Input

- *Braid index $n$, substrate parameter $q$.*

### Output

- *Length-graded decomposition
  $H_n(q) = \bigoplus_{\ell \geq 0} F_\ell / F_{\ell - 1}$ where
  $F_\ell$ is the span of basis elements $T_w$ with $\ell(w) \leq \ell$.*
- *Boolean assertion that $d_r = 0$ for all $r \geq 2$ (i.e. the
  spectral sequence collapses at the $E_2$ page).*

### Algorithm

```
1. For each ℓ from 0 to ℓ_max:
     enumerate basis elements T_w with ℓ(w) = ℓ.
2. Build the associated graded ⊕_ℓ gr_ℓ H_n(q).
3. Verify d_2 = 0 by checking that the Markov trace pairs
   gr_ℓ with gr_{ℓ + r} trivially for r > 0.
4. Return the filtration and the collapse certificate.
```

### Correctness conditions

*[`prop:gb-spectral-sequence`](#prop:gb-spectral-sequence)
asserts $E_2$-collapse for the GS filtration on $H_n(q)$ in the
QOU rigid-monoidal setting. The proof uses the diamond-lemma /
Gröbner basis structure of the Hecke relations and is standard
modulo the QOU-specific Markov coefficient $z$.*

### Complexity

*$O(\dim H_n(q))$ basis enumeration. The collapse check is
quadratic in the number of basis elements but the result is
cached per $(n, q)$ pair.*

### Python API entry point

*Canonical compute is the script
[`computations/gb_filtration_jet_tracker.py`](../../../computations/gb_filtration_jet_tracker.py);
run it directly to emit the witness. The Rust implementation
lives in [`tools/hecke-engine/`](../../../tools/hecke-engine/),
called via `pyhecke_native` when the per-particle builders need
the filtered NF.*

### Witness contract

*Canonical witness:
[`gb-filtration-jet-order.witness.json`](../../../computations/gb-filtration-jet-order.witness.json)
records the per-level filtration dimensions and the $d_2 = 0$
certificate.*

### Notes

*$E_2$-collapse is what justifies treating the GS filtration as
**exact**: any higher differential would re-mix length levels and
break the jet-order matching used by Step 8.*
<!-- FILE_END: mba-step07-gb-filtration.md -->

<!-- FILE_START: mba-step08-jet-prefix.md -->
**Algorithm (Jet-prefix transport, $q \to 1$ limit).**
*Truncate the Markov-trace Laurent polynomial at jet order $N$
and transport its leading coefficients to the archimedean fibre
at $q = q_0$ via the GS filtration of Step 7.*

### Input

- *Markov-trace polynomial $P_K(q) = \mathrm{tr}_M(\mathrm{NF}(K))$
  (output of Step 3, evaluated symbolically).*
- *Target jet order $N \in \mathbb{N}$ (chosen by precision goal —
  default $N = \lceil \log_{10}(1/\varepsilon) / 2.07 \rceil - 1$
  per AGENTS.md "$\mathfrak{Q}_\beta$ c_k truncation order").*

### Output

- *Truncated polynomial
  $P_K^{(N)}(q) = \sum_{d = -N}^{N} c_d \, q^d$ with
  $|P_K(q) - P_K^{(N)}(q)| = O(h^{N+1})$ where $h = q - 1$.*

### Algorithm

```
1. Expand P_K(q) around q = 1 as a Taylor / Laurent series in h.
2. Retain terms up to order h^N.
3. Match length levels ℓ to jet orders d via the GS-filtration
   correspondence (`prop:jet-prefix-gb-filtration`).
4. Return the truncated polynomial with jet-order metadata.
```

### Correctness conditions

1. *[`prop:jet-prefix-gb-filtration`](#prop:jet-prefix-gb-filtration)
   gives the length $\leftrightarrow$ jet-order correspondence used in step 3.*
2. *[`prop:gb-spectral-sequence`](#prop:gb-spectral-sequence) ($E_2$
   collapse, Step 7) ensures the truncation does not mix orders.*

### Complexity

*$O(N \cdot \dim H_n(q))$ — linear in the target jet order and
in the Hecke dimension.*

### Python API entry point

*Canonical compute is the script
[`computations/gb_filtration_jet_order_reader.py`](../../../computations/gb_filtration_jet_order_reader.py),
which reads the GS-filtered NF and emits the per-jet-order
truncation witness. The substrate's precision discipline (compute
at 65 dps, serialise at 50 dps) is configured by
[`qou_substrate.precision`](../../../tools/qou-substrate/python/qou_substrate/precision.py).*

### Witness contract

*Canonical witness:
[`gb-filtration-jet-order-reader.witness.json`](../../../computations/gb-filtration-jet-order-reader.witness.json).
Records the truncated polynomial, the jet-order metadata, and a
cross-check against the symbolic Taylor expansion.*

### Notes

*The jet-prefix truncation is the **gate** between symbolic
($q$-exact) compute and the archimedean evaluation at $q_0$. The
choice of $N$ is precision-driven; see the $c_k$ truncation
sidecar for the analogous truncation in the $\mathfrak{Q}_\beta$ ladder.*
<!-- FILE_END: mba-step08-jet-prefix.md -->

<!-- FILE_START: mba-step09a-mass-identity.md -->
**Algorithm (Mass identity at $q = q_0$).**
*Evaluate the absolute nucleon mass via the muon-anchored Hecke energy
(owner ruling 2026-06-24)*

$$
m_p = \dim V_{(2,1)} \cdot \bigl( m_\mu \cdot F_{\mathrm{Bor}} - |S_3| \cdot m_e \bigr), \qquad
m_\mu = m_e \cdot \mathrm{Vol}(4_1) / \hbar_q^2 ,
$$

*with the dimensionless Hecke factor
$F_{\mathrm{Bor}} = |\mathrm{tr}_M(\beta_{\mathrm{Bor}})| \cdot [3]_q! / q^3$,
via the canonical chain Steps 1 $\to$ 3 $\to$ 5 $\to$ here. This is the
**raw** identity: the substrate parameter $q_0$ is pinned by solving
exactly this form against $m_p/m_e$ (owner ruling 2026-07-03, which
stripped an earlier fitted Habiro 4-loop dressing from the pin), so the
identity round-trips $m_p$ by construction and $m_\mu$, $m_n$ are the
predictions.*

> **Fit-tier dressing (not canonical).** An optional 4-loop factor
> $R_{\mathrm{s5bb}} = (1 + c_4 u^4)(1 + 4 u^5)(1 - 29 u^6)$,
> $u = b\,\hbar_q^2$, $b = \sqrt{(q^4+q^2+1)/(q^2+1)^2}$, is retained in
> the producer (`m_p_substrate_identity_50dps.habiro_ratio_s5bb`) but is
> **fit-tier, not derived**: the exact $c_4$ that lands $m_p$ on CODATA
> is *linear in the $q_0$ pin offset* (so $c_4$ merely reparametrizes the
> $\mu$–$p$ tension), and neither $c_4 = 46$ nor $c_4 = 4143/90$ has a
> derivation trail in the corpus. Applied at the raw pin it *overshoots*
> CODATA $m_p$ by $\approx 242$ ppb. The reconcile (relabel / revert /
> drop) is owner-gated — see
> [PR #3280](https://github.com/litlfred/qou/pull/3280) and the
> [deuteron ledger](../../../docs/audits/2026-07-03-deuteron-from-scratch-error-ledger.md)
> finding 5.

### Input

- *Substrate parameter $q_0 \in \mathbb{R}_{> 1}$ (CAL-2 anchor;
  phys-obs layer pins on $m_p/m_e$).*
- *Electron mass $m_e$ in MeV (CAL-1 anchor).*
- *$\mathrm{Vol}(4_1) \approx 2.0299$ (figure-eight knot, Lobachevsky
  closed form; the muon's knot).*

### Output

- *Predicted masses $m_p, m_n \in \mathbb{R}_{> 0}$ in MeV.*

### Algorithm

```
1. Compute |tr_M(β_Bor, q)| = (4 + h² − 3h⁴ − h⁶)/(h² + 4)
   (Lean-proved closed form, BorromeanMarkovTrace.lean; h = q − q⁻¹).
2. Form F_Bor = |tr_M(β_Bor)| · [3]_q! / q³   ([3]_q! Lean-proved).
3. Muon anchor: m_μ = m_e · Vol(4₁) / ℏ_q²  (ℏ_q = 1 − q⁻¹).
4. m_p = 2·(m_μ·F_Bor − 6·m_e)   (raw identity; no habiro dressing).
5. m_n = m_p + Q_β + m_e with the parameter-free Kashiwara b²
   truncation Q_β (derived_masses.q_beta_kashiwara_n2_mev).
6. Evaluate at q = q₀ with 50-dps mpmath precision.
```

### Correctness conditions

1. *[`prop:mass-identity-exists`](#prop:mass-identity-exists) gives
   existence of the mass identity in the QOU premise.*
2. *[`prop:mass-identity-unique`](#prop:mass-identity-unique) makes
   the identity unique modulo the calibration choice.*
3. *[`thm:knot-mass-formula-unified`](#thm:knot-mass-formula-unified)
   ties the categorical scalar to the archimedean MeV observable.*

### Complexity

*Closed-form throughout (no Hecke machinery needed): sub-millisecond
at 50 dps.*

### Python API entry point

```python
from canonical_mass import proton_neutron_mass_mev

m_p_MeV, m_n_MeV = proton_neutron_mass_mev()
```

*`computations/canonical_mass.py` is the SINGLE facade (owner ruling
2026-06-24): it prefers the producer witness and falls back to the raw
identity above (no $R_{\mathrm{s5bb}}$ dressing — the fallback matches
the raw pin). Producer:
[`m_p_substrate_identity_50dps.py`](../../../computations/m_p_substrate_identity_50dps.py).*

### Witness contract

*Canonical witness:
[`m-p-substrate-identity-50dps.witness.json`](../../../computations/m-p-substrate-identity-50dps.witness.json)
(predictions $m_p, m_n, m_\mu$, CODATA anchors, ppb residuals).
Dashboard roll-up:
[`per-observable-100x-status.witness.json`](../../../computations/per-observable-100x-status.witness.json).*

### Notes

*Deprecation (owner ruling 2026-06-24, guardrail
[`canonical-mass-formula-guardrail.md`](../../../docs/canonical-mass-formula-guardrail.md)):
the volume-density forms
$m_e \cdot \mathrm{Vol}(\mathcal{B}_3) \cdot \lambda_A / \hbar_q^2$
($\approx 966$ MeV, a CODATA-implied fit) and
$m_e \cdot \mathrm{Vol}(\mathcal{B}_3) \cdot \mathrm{tr}_M / \hbar_q^2$
($\approx 406$ MeV) are NOT the absolute nucleon mass; the old
"+2.89 % $m_p$ gap" was the $\lambda_A$ fit artifact.
`vol_density_per_block` remains valid for **binding ratios only**
(the scale cancels) — the binding-side per-knot density is Step 9b's
$\Delta_\lambda$ frontier.*

*Anchor bookkeeping: at the proton-pinned $q_0$ the $m_p$ value is an
anchor round-trip (exact in ratio space), $m_\mu$ and $m_n$ are the
predictions; the pin's Habiro dressing reconciles the muon identity to
$\approx 1.4$ ppb (per-stage attribution in the
[2026-07-03 deuteron ledger](../../../docs/audits/2026-07-03-deuteron-from-scratch-error-ledger.md);
the $c_4$ pin-vs-producer 46 vs $4143/90$ reconcile is owner-gated,
bean `2i8g`).*

*Linking-weight selection rule (binding-side, retained for Step 9b):
the factor
$\mathrm{lw}(c) = \frac{1}{c+1}\sum_{\lambda \vdash c+1} \dim_q V_\lambda$
reproduces $\mathrm{lw}(1)=1$ (muon) and
$\mathrm{lw}(3) = (3q^2+4+3q^{-2})/4$ (Family-A — bit-for-bit equal to
`linking_weight_family_a`, now deprecated for absolute mass), and gives
$\mathrm{lw}(2) = (q+1)^2/(3q)$
([`prop:selection-rule-c2-prediction`](../climax-volume-mass/selection-rule-c2-prediction.md)).
Regression-tied to production by
[`binding_selection_rule_tau_closure.py`](../../../computations/binding_selection_rule_tau_closure.py)
$\to$ [witness](../../../computations/binding-selection-rule-tau-closure.witness.json).
The same $\mathrm{lw}(c)$ values are the SW-period anchors of the
depth-2 binding kernel — see
[`mba-step09b`](mba-step09b-per-isotope-binding.md).*
<!-- FILE_END: mba-step09a-mass-identity.md -->

<!-- FILE_START: mba-step09b-per-isotope-binding.md -->
**Algorithm (Per-isotope binding energy, conditional on $\Delta_\lambda$).**
*Evaluate the binding energy
$B(K) = m_e \cdot \sum_\lambda y_\lambda(q_0)\, \chi^\lambda(K)\, \Delta_\lambda(K)$
for an isotope-coded knot $K$ via the Wedderburn-Frobenius
decomposition plus the per-partition binding density
$\Delta_\lambda$.*

### Input

- *Isotope knot $K$ (canonical braid encoding — see
  Appendix Knot Periodic Table).*
- *Substrate $q_0$, electron mass $m_e$ (CAL-1, CAL-2 anchors).*
- *Per-partition $\Delta_\lambda(K)$ — currently **open**, see
  `alg:delta-lambda-closure` sidecar.*

### Output

- *Predicted binding energy $B(K) \in \mathbb{R}_{> 0}$ in MeV.*

### Algorithm

```
1. Compute the partition-decomposition (Step 5) at the isotope's
   braid index n_K.
2. For each λ ⊢ n_K:
   a. Compute y_λ(q_0) (Wedderburn weight).
   b. Compute χ^λ(K) via the Step 3 fine-Bratteli transfer matrix
      (lossless over all λ ⊢ n_K; no d_λ Hoefsmit rep materialised).
   c. Look up Δ_λ(K) from the candidate closure ansatz
      (currently: Option-E / crystal — see sidecar).
3. Sum λ contributions and multiply by m_e.
```

### Correctness conditions

1. *[`rem:term6-binding-density`](#rem:term6-binding-density)
   gives the binding-density formula at $q = q_0$.*
2. *[`thm:knot-mass-formula-unified`](#thm:knot-mass-formula-unified)
   ties the partition sum to the archimedean MeV observable.*

*The remaining conjectural input is $\Delta_\lambda(K)$ itself —
six closure ansätze (Frobenius co-Casimir, Demazure-fibre,
LP-Plancherel, LP-Frobenius, crystal-graph, augmented Markov)
have all failed on the deuteron. The current
direction is Option E (Kashiwara crystal) — see
`alg:delta-lambda-closure`.*

### Complexity

*The $\chi^\lambda$ trace (step 2b) is computed by the Step 3
transfer matrix — a fine-Bratteli edge sweep (a few thousand edges
at $n = 21$), not the $d_\lambda$-dimensional Hoefsmit
representation — so the per-isotope cost is the partition count
$p(3A)$ times that sweep, not $n!$. Mass-table sweeps therefore
reach $A \geq 6$ ($^6$Li $\approx 0.2$ s, $^7$Li $\approx 0.6$ s),
where the former per-basis-vector path hit the $d_\lambda$ wall
(markov\_peel $\approx 17$ min at $^6$Li). The open gate is
$\Delta_\lambda$ (step 2c), not the trace compute.*

### Python API entry point

```python
from qou_mass import predict

p = predict(atom="deuteron", observable="binding_energy")
B = p.value   # MeV
```

*Binding-energy is selected by the `observable` keyword on the
unified `predict()` entry point; there is no separate
`binding_energy(...)` function. The mass-table sweep is the
script [`canonical_mass_table_extended.py`](../../../computations/canonical_mass_table_extended.py).
Its `--method auto` routes per-atom over the mixed nucleon+composite
set: free nucleons ($A < 2$) use the direct $H_3$ Hoefsmit path
`laurent_q_rust` (pyhecke-native Rust + MPFR); composites ($A \geq 2$)
use the `branching` combiner, whose $\chi^\lambda$ comes from the
operator-valued Wenzl recursion at $A = 2$ and the lossless
fine-Bratteli transfer matrix at $A \geq 3$ (`chi_monotone_transfer` —
all $p(3A)$ partitions at 50 dps, no $d_\lambda$ wall, pure mpmath, with
the color-weighted p-n crossing handled internally). All routes are MPFR
at the 50-dps floor; `auto` is the only setting that spans a table mixing
free nucleons and composites in one run.*

*The **graded-ρ_K atomic-mass route** ([`prop:rho-k-graded-expansion`](../mass-endomorphism/rho-k-graded-expansion.md))
is realised by [`rho_k_graded_atomic_mass.py`](../../../computations/rho_k_graded_atomic_mass.py)
(witness `rho-k-graded-atomic-mass.witness.json`): LO constituents from the
canonical `canonical_mass` facade + the proved single-gen correction
$\alpha \sum_i \ln|\hat V_i^{\mathrm{full}}|$ ($0.19\%$ mean, $Z = 1..10$);
the pair-gen tier is reported as the open residual only, never wired.*

### Witness contract

*Provisional witness:
[`canonical-mass-table-242ppb.witness.json`](../../../computations/canonical-mass-table-242ppb.witness.json).
Records per-isotope predicted $B(K)$, the AME experimental anchor,
and an explicit `"open_gate": "delta_lambda"` flag marking
$\Delta_\lambda$ as the open Track-A gate. It is a hand-authored
summary (`auditOnly`, no producer run): the $B(K)$ values are not a
derived $\Delta_\lambda$ result and await a producer-backed
regeneration once the $\Delta_\lambda$ closure lands.*

### Notes

*This is the **Track A blocker**: $\Delta_\lambda$ closure is the
single open piece preventing the per-isotope binding from
reaching L2 (100× L2 target) for the four currently-missing
observables. See [`docs/audits/2026-05-18-delta-lambda-gating-context.md`](../../../docs/audits/2026-05-18-delta-lambda-gating-context.md).*

*Inter-nucleon interface convention (canonical default): the p-n
averaged crossing is **color-weighted**, $\sigma - h\,(1/2 - \delta/4)\cdot\mathbf{1}$
with $\delta = $ `flavor_split_subleading`$(q_0)$ (the substrate
$(m_n - m_p)/M_N$ flavor split), set in
[`mass_at_3A_proper.atom_braid_word_3A`](../../../computations/mass_at_3A_proper.py)
(`pn_convention="bring_color_weighted"`). The p-p ($\sigma$) and
n-n ($\sigma^{-1}$) interfaces are isospin-distinct and carry no
extra color weight. The color shift is at the $\Delta m_{pn}$ scale
($\delta/4 \approx 3.4\times10^{-4}$) — not the dominant binding
residual, which is the inter-nucleon multiplicity (the linear-chain
$A-1$ consecutive-bond count, [`prop:linear-chain-bond-count`](../mass-theory/linear-chain-bond-count.md))
plus per-bond growth. See
[`docs/audits/2026-06-03-color-averaging-wiring-audit.md`](../../../docs/audits/2026-06-03-color-averaging-wiring-audit.md)
and [`docs/audits/2026-06-03-nuclear-a3-dpn-plan.md`](../../../docs/audits/2026-06-03-nuclear-a3-dpn-plan.md).*

*Production wiring (atom-trace compute): the canonical color-weighted
$\mathrm{tr}_M(\beta_{\text{atom}})$ feeding step 2b is assembled by
[`tr_m_atom_via_transfer.tr_m_atom_zn`](../../../computations/tr_m_atom_via_transfer.py),
through which the binding consumers
[`binding_canonical`](../../../computations/binding_canonical.py)
(default path) and
[`canonical_tr_m_via_branching`](../../../computations/canonical_tr_m_via_branching.py)
($A \geq 3$) now route — replacing the symbolic `tr_M_element` and
the native `chi_lambda_all_partitions_mpfr` per-partition paths.
Lossless (all $p(3A)$ partitions kept; the active-set truncation is a
$\sim10^{-3}$ error rejected for 1-ppQ per
[`docs/audits/2026-06-10-binding-active-set-compute-optimization.md`](../../../docs/audits/2026-06-10-binding-active-set-compute-optimization.md)),
validated $\mathrm{tr}_M$-transfer $\equiv$ full Hoefsmit
(`char_fast`) to $4.7\times10^{-15}$.*

*Extensive (log-free-energy) functional — the on-scale sibling.* The
$\Delta_\lambda$ sum above is the (gated) Path-D binding. A complementary
**extensive** functional on the *same* canonical $\mathrm{tr}_M$ is the
q-heat-flow free energy
$B(K) = E_0\,\log\!\big(|\mathrm{tr}_M(\beta_{\mathrm{free}})| /
|\mathrm{tr}_M(\beta_{\mathrm{atom}})|\big)$, with
$E_0 = m_e/(q_0(q_0-1)) \approx 4.186$ MeV (closed substrate form, **no fit**),
computed by
[`binding_log_free_energy.py`](../../../computations/binding_log_free_energy.py)
$\to$ [`binding-log-free-energy.witness.json`](../../../computations/binding-log-free-energy.witness.json).
It is **on-scale** ($0.57$–$2.36\times$ AME over D/T/³He/⁴He), wired onto the
canonical lossless trace rather than the per-bond $f_{\mathrm{bond}}$ product
of the exploratory probe. By contrast the canonical *linear* trace difference
$Q_\beta(\mathrm{tr}_{\mathrm{free}}-\mathrm{tr}_{\mathrm{atom}})$ is
**intensive** and saturates ($\sim0.78$ MeV, $4.8$–$39.7\times$ miss). This is
**not** a closure: the chain-topology residual (edge-set / fractional
occupancy, see
[`docs/audits/2026-06-10-binding-bond-graph-compute-audit-and-derivation.md`](../../../docs/audits/2026-06-10-binding-bond-graph-compute-audit-and-derivation.md)
§6) is the open piece. It is the on-scale sibling skipped by the 2026-06-16/17
binding-closure docs.*

*Body-order generating function — the depth-2 selection-rule kernel.* The
body-order binding series $B(K)=\sum_n B_n$ has generating function
$G(x;q)=\sum_n B_n x^n$ satisfying the fibre q-difference equation
$G(qx)=R(q,x)\,G(x)$ with $R(q,x)=x^2-\tau x+1$ — depth 2 (S₅/A₅ Schur) and
$\det=1$ (symplectic, `prop:sl2-prolongation-recurrence`, sorry-free). Its
SW-period anchors are the SAME selection-rule values
$a_D^{(n)}=\mathrm{lw}(n-1)$ that supply the
[`mba-step09a`](mba-step09a-mass-identity.md) mass linking weight:
$a_D^{(2)}{=}1$, $a_D^{(3)}{=}(q{+}1)^2/(3q)$, $a_D^{(4)}{=}$Family-A, giving
$\tau(q_0)=2.6424$
([`binding_selection_rule_tau_closure.py`](../../../computations/binding_selection_rule_tau_closure.py)).
The **algebraic** half — that these wired anchors force the closed form
$\tau=3(3q^4+8q^2+3)/(4q(q+1)^2)$ and $\tau>2$ for all $q>0$, hence the depth-2
kernel is **extensive** ($\lambda_+>1$ via the spectral bridge
`QOU.Mass.lambdaPlus_gt_one`) — is now sorry-free in Lean
(`QOU.Mass.BindingTauAnchorClosure`: `tauAnchor_closed_form`, `tauAnchor_gt_two`,
`binding_extensive_at_substrate`; lean-direct exit 0).
**Residual (open):** the geometric↔algebraic identification
$a_D^{(n)}=\mathrm{lw}(n-1)$ — that the SW prolonged period *equals* the
selection-rule value (#1765) — is not closed.*

*Body-order multiplicity — the linear-chain bond count (derived, Lean).* The
per-body-order weight of the jet-filtration residue,
$w_n(K)=M_n(A)\cdot\mathrm{Vol}_n(K)$, has its multiplicity **derived** as the
inter-nucleon bond count $M_n=n-1$: the canonical atomic braid is a **linear
chain** of $A$ nucleon blocks (joined at generators $3k-1$,
[`mba-step08`](mba-step08-jet-prefix.md) / the atomic-braid recipe), so the
consecutive $n$-clusters number $A-n+1$ and each carries $n-1$ bonds. The
aggregate cluster measure is $\sum_{n=2}^{A}(A-n+1)(n-1)=\binom{A+1}{3}$, proved
sorry-free in Lean ([`prop:linear-chain-bond-count`](../mass-theory/linear-chain-bond-count.md),
`QOU.Mass.linear_chain_cluster_measure`). With the isospin-carrying hyperbolic
sub-link volumes this reproduces the **tritium (p-n-n)** binding to within $0.16\%$
with **no fitted constant** ([`theta_mn_bondcount_linearchain.py`](../../../computations/theta_mn_bondcount_linearchain.py));
³He to $-3\%$; the deuteron 2-body bond is the Hopf link ($\mathrm{Vol}=0$) — a
structural exception. This is a $\sim3\%$ *structural* result, not a ppQ closure.

> **Convention resolved — linear chain, not all-pairs.** An earlier phrasing
> attributed the binding multiplicity to the all-pairs $\binom{A}{2}$ bond count.
> The atomic-braid recipe settles it: the *inter-nucleon crossing rule* places a
> single interface crossing at generator $3k-1$ for $k=1..A-1$, so the bonds sit at
> $\{2,5,8,\ldots\}$ — $A-1$ **consecutive** bonds (deuteron $1$; $^4$He $3$ at gens
> $2,5,8$, **not** $\binom{4}{2}=6$; verified
> [`theta_mn_linearchain_vs_allpairs.py`](../../../computations/theta_mn_linearchain_vs_allpairs.py)).
> The structure is the path graph $P_A$, **not** the complete graph $K_A$; the
> multiplicity is the linear-chain $A-1$ with the $\binom{A+1}{3}$ body-order
> aggregate ([`prop:linear-chain-bond-count`](../mass-theory/linear-chain-bond-count.md),
> Lean-proved), which reproduces $^3$H (p-n-n) to within $0.16\%$ with no fit. A
> distinct all-pairs mean-field model, if wanted, would need its own derivation —
> the canonical braid does not realise one.
<!-- FILE_END: mba-step09b-per-isotope-binding.md -->

<!-- FILE_START: mba-step10-confinement-sdp.md -->
**Algorithm (Confinement SDP — canonical $T_w$).**
*Solve the LP/SDP that selects the canonical Hecke element $T_w$
realising confinement (or gluon attachment, electron attachment,
molecular bonding — the universal ILP of Algorithm
$\mathtt{def:universal-ilp-algorithm}$).*

### Input

- *Current state $x \in H_n(q)$ (Hecke normal form — Step 2).*
- *Gram matrix $G_{ij} = \mathrm{tr}_M(b_i \cdot b_j)$ computed once
  via Step 6.*
- *Markov-trace vector $t_i = \mathrm{tr}_M(b_i)$.*
- *Target net constraint $n_{\mathrm{target}} \in \mathbb{Z}_{\geq 0}$.*

### Output

- *Primal: optimal $x^* \in \mathbb{R}_{\geq 0}^{\mathrm{cols}(G)}$.*
- *Dual: shadow prices $y_0^*$ (net constraint) and
  $y^*_i \geq 0$ (Frobenius positivity).*
- *Active set: $\{i : y^*_i > 0\}$ — the "receptive sub-braids".*
- *`primal_obj`, `dual_obj`, `duality_gap = |primal_obj − dual_obj|`.*

### Algorithm

```
1. Build LP:
   minimize   Σ_i t_i x_i
   subject to net(x) = n_target,
              G x ≥ 0,
              x ≥ 0.
2. Solve via Clarabel (default) or a sibling SDP backend.
3. Recover dual variables y_0*, y*.
4. Emit the LP-dual witness (per AGENTS.md "LP/SDP duals —
   first-class infra").
```

### Correctness conditions

*[`prop:operator-selection-lp`](#prop:operator-selection-lp)
specifies the LP and proves the canonical $T_w$ is its primal
optimum. Strong duality gives `primal_obj = dual_obj` (modulo
solver tolerance); the active dual variables identify the
binding-energy shadow prices that feed Step 9b.*

### Complexity

*Polynomial in $\dim H_n(q)$. Clarabel solves the proton-scale
LP in milliseconds.*

### Python API entry point

*Canonical compute is the script
[`computations/confinement-operator-selection.py`](../../../computations/confinement-operator-selection.py),
which solves the LP with primal + dual emission and writes
`confinement-operator-selection.witness.json`. The reusable
solver helpers are exposed as
`pyhecke.lp_dual_solver.solve_operator_selection_lp(t, G, n_target)`
(in [`tools/pyhecke/python/pyhecke/lp_dual_solver.py`](../../../tools/pyhecke/python/pyhecke/lp_dual_solver.py)).*

### Witness contract

*Canonical witness:
[`confinement-operator-selection.witness.json`](../../../computations/confinement-operator-selection.witness.json).
**Must emit all of** `y0_star`, `y_star`, `active_set`,
`primal_obj`, `dual_obj`, `duality_gap` — enforced in CI by
[`lp_dual_witness_validator.py`](../../../computations/lp_dual_witness_validator.py)
(see AGENTS.md "LP/SDP duals — first-class infra").*

### Notes

*The active dual variables $y^*_i > 0$ name the "most receptive
sub-braids" — they are the structural identifiers of the
saturated Wedderburn blocks. Solving only the primal loses this
information; the dual emission is **required**, not optional.*
<!-- FILE_END: mba-step10-confinement-sdp.md -->

<!-- FILE_START: mba-step11-q-beta-truncation.md -->
**Algorithm ($\mathfrak{Q}_\beta$ truncation ladder).**
*Evaluate $\beta$-decay $Q$-values via the convergent series
$\mathfrak{Q}_\beta = Q_{\mathrm{base}} \cdot \prod_{k = 2}^{N} (1 + c_k\, u^k)$
with $u = b \cdot \hbar_q^2 \approx 0.00852$, truncating at order
$N$ chosen by the target precision.*

### Input

- *Decay channel (parent isotope $A \to$ daughter $A'$).*
- *Substrate $q_0$, electron mass $m_e$ (CAL-1, CAL-2).*
- *Pion decay width (CAL-3) for $\mathfrak{D}_\pi$.*
- *Target precision $\varepsilon \in \mathbb{R}_{> 0}$ → truncation
  order $N \geq \lceil \log_{10}(1/\varepsilon) / 2.07 \rceil - 1$.*

### Output

- *$\mathfrak{Q}_\beta \in \mathbb{R}$ in MeV.*

### Algorithm

```
1. Compute Q_base from the substrate identity m_e · (m_n / m_e)
   modulo the binding-energy contribution.
2. Compute u = b · ℏ_q² where ℏ_q is the q-quantum constant.
3. For k = 2, …, N:
   c_2 = -1                  (Taylor-exact, PROVED).
   c_k for k ≥ 3 are q_0-dependent NEAR-MATCHES (see AGENTS.md
     "\mathfrak{Q}_\beta c_k is a TRUNCATION ORDER, not a wire/un-wire gate").
   Multiply Q_base by (1 + c_k · u^k).
4. Return \mathfrak{Q}_\beta.
```

### Correctness conditions

*[`prop:q-beta-categorical-precision-ladder`](#prop:q-beta-categorical-precision-ladder)
establishes the precision ladder and the convergence rate.*

*The $c_k$ coefficients are **tiered**:*

- *$c_2 = -1$: **proved** Taylor-exact.*
- *$c_k$ for $k \geq 3$: **near-match** with $q_0$-dependent
  swings (e.g. $c_3 = -2 = J_{\mathrm{Hopf}}(q = 1)$ within
  $\sim 3\%$ at the m_p-pin $q_0$).*
- *$c_k$ never reported as "fitted" — see
  [`docs/audits/2026-05-31-qbeta-ck-truncation-order-canonical-framing.md`](../../../docs/audits/2026-05-31-qbeta-ck-truncation-order-canonical-framing.md).*

### Complexity

*$O(N)$ — linear in truncation order.*

### Python API entry point

*Canonical compute is the script
[`computations/q_beta_predicted.py`](../../../computations/q_beta_predicted.py);
run it directly to emit the per-channel witness. The CAL-3 pin is
generated by [`build_cal_3_q_beta_witness.py`](../../../computations/build_cal_3_q_beta_witness.py).*

### Witness contract

*Canonical witnesses: [`cal-3-q-beta.witness.json`](../../../computations/cal-3-q-beta.witness.json)
(CAL-3 pin) and [`q-beta-predicted.witness.json`](../../../computations/q-beta-predicted.witness.json)
(per-channel predictions). Both report the truncation order $N$
used and the tiered $c_k$ classification.*

### Notes

*The **production neutron mass** consumes a closed-form partial
resummation of this ladder — the parameter-free **Kashiwara $b^2$**
truncation
$\mathfrak{Q}_\beta = Q_A \cos(\alpha - b\,\hbar_q^2/2)\,(1 - b^2 \hbar_q^4)$
([`derived_masses.q_beta_kashiwara_n2_mev`](../../../computations/derived_masses.py),
wired into the neutron via [`canonical_mass.py`](../../../computations/canonical_mass.py)
and [`m_p_substrate_identity_50dps.py`](../../../computations/m_p_substrate_identity_50dps.py)).
Its outer factor $(1 - b^2\hbar_q^4) = (1 - u^2)$ is exactly the
$c_2 = -1$ term of the ladder above (with $u = b\,\hbar_q^2$); the $\cos$
factor supplies the odd-$b$ ($N{=}1$) correction.*

*L2 status (live, PR #2723): $\mathfrak{Q}_\beta$ at $\sim 160\times$ miss
(1248 ppb, $+1.25\,\mathrm{ppm}$ on $\mathfrak{Q}_\beta$) and $m_n$ at
$\sim 181\times$ miss ($+1.04\,\mathrm{ppb}$) vs the (research-grade,
sub-CAL-2-floor) 100× targets — both improved $\sim 1690\times$ over the
former flavor-split route. TIER: **near-match**; exact closure gated on
the s5-so3 / Habiro keystone (`conj:s5-so3-fiber-action`, bean s5bb).
Supersedes the earlier "164.0× as of 2026-05-31 / Habiro-exact 5.7 ppb at
the pre-re-pin muon anchor" note.*
<!-- FILE_END: mba-step11-q-beta-truncation.md -->

