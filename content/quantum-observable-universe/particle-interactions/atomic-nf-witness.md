## Normal form witness

**Proposition.**
*For each atom $(Z, N)$ with $Z = 1$--$20$, the atomic braid
construction produces an element of $H_{A+Z}(q)$ that is verified
to be in Gröbner–Shirshov normal form.  Specifically:*

1. *The ground-state nucleon ordering is the global minimum of
   $\Phi_1$ over all $\binom{A}{Z}$ permutations (exact for
   $\binom{A}{Z} \leq 50000$, steepest descent otherwise).*

2. *Each electron is inserted at the position minimizing $\Phi_1$
   (greedy, verified to produce ep pairs adjacent to protons).*

3. *At each construction step (adding strand $k$ with crossings
   to all previous strands $0, \ldots, k-1$): the
   Gröbner–Shirshov reduction is run to convergence
   ([inductive reduction](#inductive-gb-reduction)).  Convergence
   is guaranteed by the Diamond Lemma (the three rewriting rules
   satisfy all overlap ambiguities).*

4. *The final NF element is accumulated without mid-construction
   stripping for $A \leq 9$ (exact).  For $A > 9$, the element is
   stripped at controlled thresholds (200k--500k words) and the
   stripped contributions are accumulated into the Pauli character
   $F_{\mathrm{Pauli}} = |\mathrm{tr}_{\mathrm{alt}}/\mathrm{net}|$.*

5. *Certificates (JSON) are committed to the repository for each
   computed atom.  Each certificate records: $F_{\mathrm{Pauli}}$,
   $\mathrm{tr}_{\mathrm{alt}}(q_0)$, $\mathrm{net}(q_0)$,
   computation time, word count, and engine version.*

*The three Wedderburn invariants $\Phi_1$, $\Phi_2$, $\Phi_3$ used
in the mass formula
([three-invariant mass formula](#prop:wedderburn-mass-formula))
are computed from the transfer matrix chain, which incorporates the
Hecke relation $\sigma_i^2 = (q - q^{-1})\sigma_i + \mathbf{1}$
at each crossing.  The transfer matrix output is in normal form by
construction: the $2 \times 2$ matrix product automatically absorbs
all Hecke reductions into the matrix entries.*


## Step-by-step LP stability verification

*Each atom is verified to be LP-stable at every construction step.
For each strand $k$ added to the braid:*

- *The three Wedderburn channels (symmetric, standard, alternating)
  are computed independently.*
- *No channel eigenvalue product is zero at any step.*
- *The symmetric and alternating channels maintain distinct signs,
  preventing the channel-mixing annihilation that destabilises the
  bare hydrogen atom.*

*Verified atoms (all 20 pass all-channel-nonzero at every step):
${}^1\mathrm{H}$, ${}^4\mathrm{He}$, ${}^7\mathrm{Li}$,
${}^9\mathrm{Be}$, ${}^{11}\mathrm{B}$, ${}^{12}\mathrm{C}$,
${}^{14}\mathrm{N}$, ${}^{16}\mathrm{O}$, ${}^{19}\mathrm{F}$,
${}^{20}\mathrm{Ne}$, ${}^{23}\mathrm{Na}$, ${}^{24}\mathrm{Mg}$,
${}^{27}\mathrm{Al}$, ${}^{28}\mathrm{Si}$, ${}^{31}\mathrm{P}$,
${}^{32}\mathrm{S}$, ${}^{35}\mathrm{Cl}$, ${}^{40}\mathrm{Ar}$,
${}^{39}\mathrm{K}$, ${}^{40}\mathrm{Ca}$.*

*Full LP stability (existence of an annihilator in the complete
$H_n(q)$) is verified for ${}^1\mathrm{H}$ (dressed, stable),
proton $\mathfrak{p}$ (stable), and neutron $\mathfrak{n}$
(stable).*

**Witness**: `atom-mass-complete-wedderburn.witness.json`,
Rust certificates in `tools/hecke-engine/certificate-*.json`.
