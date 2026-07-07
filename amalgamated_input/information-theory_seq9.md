<!-- FILE_START: phase-transitions-intro.md -->
The quantum ideal gas law yields a partition function whose dominant saddle point sits inside one Hecke channel of $H_n(q)$. Phase transitions form the loci where this dominance changes. We compute critical temperatures using the $S^3$ boundary action. This restricts the categorical action to the Hopf base $S^2$ of the fibration $S^1 \hookrightarrow S^3_q \to S^2$. The quantities $[2]_q$ and $[n_K]_q$ control $T_q^{(g \to l)}$ and $T_q^{(l \to s)}$.

We map gas, liquid, and solid states to the symmetric, mixed, and antisymmetric Hecke channels, and locate the triple point. We then derive sublimation (the direct solid--gas transition) using a non-split extension classified by $\mathrm{Ext}^1_{H_n(q)}$. We present an observational test of the $Z$-parity sublimation rule, establishing a metallic-bonding test that separates sublimation from continuous condensation. Finally, we explore incompleteness and the horizon. This treats the phase-transition boundary as a canonical example of degree-$0$ opacity in statistical mechanics. _(draft.)_
<!-- FILE_END: phase-transitions-intro.md -->

<!-- FILE_START: phase-transition-boundary.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with $N$ particle knots in a region $U$. A **phase transition** occurs at a critical temperature $T_q^{(c)}$. At this temperature, the dominant saddle point of the partition function $Z_q$ jumps discontinuously between topologically distinct sectors of $\mathrm{Conf}(U)$.

The **$S^3$ boundary action** determines the critical temperatures. It restricts the categorical action $\mathfrak{S}_q$ to the Hopf base $S^2$ of the fibration $S^1 \hookrightarrow S^3_q \to S^2$:

$$
  \mathfrak{S}_q^{(\partial)}
  \;:=\;
  \mathrm{tr}_{\mathrm{Ad}}
  \!\oint_{S^2}
  \omega_{\mathcal{F}} \,\wedge\, *\eta_q,
$$

This integral is the non-abelian Stokes surface integral of the adjoint connection ([Yekutieli triple](#def:yekutieli-triple)).

The gas--liquid critical temperature is

$$
  T_q^{(g \to l)}
  \;=\;
  \frac{\mathfrak{S}_q^{(\partial)}}{[2]_q}.
$$

The liquid--solid critical temperature is

$$
  T_q^{(l \to s)}
  \;=\;
  \frac{\mathfrak{S}_q^{(\partial)}}{[2]_q \cdot [n_K]_q},
$$

where $n_K$ is the crossing number of the particle knot.

Sublimation is a direct solid--gas transition. It occurs when topological obstruction blocks the intermediate liquid phase. In this case, the Hecke representation at the mixed-channel temperature admits a non-split extension:

$$
  0 \;\to\; V_{\mathrm{sym}} \;\to\;
  V_{\mathrm{mixed}} \;\to\;
  V_{\mathrm{asym}} \;\to\; 0
$$

This extension is classified by $\mathrm{Ext}^1_{H_n(q)}(V_{\mathrm{asym}}, V_{\mathrm{sym}}) \cong \mathbb{Z}$. The Hopf invariant of $\pi_3(S^2) = \mathbb{Z}$ generates it.
<!-- FILE_END: phase-transition-boundary.md -->

<!-- FILE_START: composite-crossing-parity.md -->
**Proposition (conditional on [conj:borromean-quark](#conj:borromean-quark)).** Let $\mathcal{A}(Z, N)$ be a stable atom with electron configuration occupying shells $S_1, \ldots, S_k$. The complete decomposition ([knot eigenbasis](#prop:knot-eigenbasis-complete))

$$
  V^{\otimes n} \cong
  \bigoplus_{\lambda \vdash n,\, \ell(\lambda) \leq 2}
  V_\lambda \otimes S_\lambda
$$

determines both the nuclear shell structure ([shell eigenvalues](#prop:shell-structure-eigenvalues)) and the thermodynamic phase behavior ([phase transitions](#prop:phase-transition-boundary)) through the same Hecke algebra $H_n(q)$.

**Sublimation criterion.**
An atom sublimes—bypassing the liquid phase—when the Hecke module at the mixed-channel temperature admits a non-split extension ([phase transitions](#prop:phase-transition-boundary)). This extension is classified by

$$
  \mathrm{Ext}^1_{H_n(q)}(S_{\mathrm{asym}},
  S_{\mathrm{sym}}) \;\cong\; \mathbb{Z}.
$$

The extension **splits** (yielding a stable liquid phase) if and only if the outermost electron shell is closed or nearly closed. In terms of partitions, the Young diagram $\lambda_{\mathrm{outer}}$ labelling the valence electrons must satisfy $\lambda_1 - \lambda_2 \leq 1$. Equivalently, the valence shell sits in the symmetric or near-symmetric sector of the Schur--Weyl decomposition.

The extension is **non-split** when the valence shell is half-filled ($\lambda_1 \approx \lambda_2 + n/2$). Here the mixed Hecke channel achieves maximal dimension, driving sublimation.

**Crossing parity.**
To estimate sublimation behavior, we check the composite crossing parity. The composite crossing number satisfies $n_K(\mathcal{A}) \equiv Z \pmod{2}$, following from the crossing budget $A^2 + 7A + 5Z$ and the identity $A(A+1) \equiv 0 \pmod{2}$. This parity detects the mod-2 shadow of the Young diagram structure. It is a necessary but not sufficient condition for sublimation because it cannot distinguish closed shells from half-filled ones.

**Full criterion.**
Let $\ell_v$ denote the number of valence electrons beyond the last closed shell ([noble gas characterization](#prop:noble-gas-characterization)). Let $\ell_{\max}$ be the capacity of the valence shell ($\ell_{\max} = 2n^2$ for principal quantum number $n$). We classify the macroscopic phase:

1. **Closed shell** ($\ell_v = 0$ or $\ell_v = \ell_{\max}$): The extension splits. The liquid phase is stable.
2. **Near-closed shell** ($\ell_v = 1$ or $\ell_v = \ell_{\max} - 1$): The extension splits via the closed-core trivializing section. The liquid phase is stable.
3. **Half-filled shell** ($\ell_v \approx \ell_{\max}/2$) with odd $Z$: The extension is non-split. The atom is prone to sublimation.
4. **Metallic band** (delocalized electrons): The single-atom Hecke module $S_\lambda$ is replaced by the band-structure module $\bigoplus_k S_{\lambda(k)}$ over crystal momenta $k$. The direct sum generically contains both split and non-split extensions. The split extensions dominate, yielding a stable liquid phase.
<!-- FILE_END: composite-crossing-parity.md -->

<!-- FILE_START: phase-transition-interpretation.md -->
The Hecke algebra $H_n(q)$ has irreducible representations corresponding to Young diagrams. At a generic temperature $T_q$, one representation dominates the partition function. At a critical temperature $T_q^{(c)}$, two representations contribute equally, producing a non-analyticity in the partition function.

**The three phases.**

1. **Gas (symmetric channel, eigenvalue $q$).**
   At high $T_q$, each knot is confined to a single $S^3$ fibre. The equation of state is the quantum ideal gas law ([quantum ideal gas law](#prop:quantum-ideal-gas-law)).

2. **Liquid (mixed channel).**
   At intermediate $T_q$, knots begin to Hopf-link across fibres through the Hopf base $S^2$. This inter-fibre linking creates correlations.

3. **Solid (antisymmetric channel, eigenvalue $-q^{-1}$).**
   At low $T_q$, inter-fibre links dominate. Knots form a rigid braid lattice, occupying the sign representation.

**Sublimation mechanism.**
When the crossing number $n_K$ is odd, the Hecke extension at the mixed-channel temperature is non-split. The Hopf invariant classifies this extension. The liquid phase becomes unstable, forcing the system to jump directly from solid to gas.

**Triple point.**
All three phases coexist when three Hecke representations contribute equally. This represents a codimension-2 condition in the $(T_q, P_q)$ plane. It obeys the Gibbs phase rule.

**Classical theory comparison.**
Classical theory generates phase transitions by adding *ad hoc* inter-particle potentials (such as van der Waals or Lennard-Jones) to the ideal gas. The QOU generates interactions through inter-fibre braid linking across the Hopf base of $S^3_q$. The $S^3$ topology supplies the "potential" via its boundary action. The Hecke representation theory supplies the discrete phase structure.
<!-- FILE_END: phase-transition-interpretation.md -->

<!-- FILE_START: crossing-parity-test.md -->
The full sublimation criterion ([shell-filling criterion](#prop:composite-crossing-parity)) relies on the Hecke representation structure, not merely the crossing parity. The determining variable is the **valence electron count** $\ell_v$ relative to the shell capacity $\ell_{\max}$.

**Test against observed sublimation at 1 atm.**

See [Table](#tbl:crossing-parity-test-table-data).

**Score: 11/12 (92%).**

The representation-theoretic criterion resolves all three counterexamples where the crude parity rule fails:

- **H** ($\ell_v = 1$ of $\ell_{\max} = 2$): The shell is near-closed. The extension splits via the trivializing section. Liquid H exists at 20 K. $\checkmark$
- **Na** ($\ell_v = 1$ of $\ell_{\max} = 2$): The shell is near-closed and exhibits metallic band delocalization. It melts normally. $\checkmark$
- **Cu** ($3d^{10}4s^1$): The $3d$ subshell is fully closed. The single $4s$ valence electron is near-closed and metallic. It melts normally. $\checkmark$

**The molecular exception: iodine.**
Iodine ($\ell_v = 5$ of $\ell_{\max} = 6$) has a near-closed shell. The atomic criterion predicts a stable liquid, yet iodine sublimes at 1 atm. This exception occurs because iodine forms a molecular $I_2$ van der Waals solid. The weak intermolecular binding makes sublimation favorable. The single-atom Hecke module is the wrong fundamental unit. The $I_2$ dimer has crossing number $n_K(I_2) \equiv 0 \pmod{2}$, but the inter-dimer linking is too weak to sustain a liquid phase. The sublimation is molecular, not atomic.

**Connection to magic numbers.**
The decomposition $V^{\otimes n} \cong \bigoplus_\lambda V_\lambda \otimes S_\lambda$ produces the nuclear magic numbers (2, 8, 20, 28, 50, 82, 126) via palindromic Poincaré polynomials in the Bruhat lattice. The identical decomposition produces the sublimation criterion via Ext groups between the irreducible summands $S_\lambda$. Magic shell closures trivialize the extension; half-filled shells maximize it.
<!-- FILE_END: crossing-parity-test.md -->

<!-- FILE_START: van-der-waals-hopf-channel.md -->
**Definition (Hopf symmetric block $e_+$).** *In the 2-strand inter-molecular Hecke algebra $H_2(q)$ (two molecules = two strands), the **symmetric (Hopf) block** is the idempotent:*

$$
  e_+ \;=\; \frac{\sigma + q^{-1}}{q + q^{-1}},
  \qquad \sigma \mapsto q \ \ (\text{trivial rep}),
$$

*the Hopf $/[2]_q$ block. Its complement is the directional (hydrogen-bond) block $e_- = (q-\sigma)/(q+q^{-1})$ (sign rep, $\sigma\mapsto -q^{-1}$).*

The Hopf link $\mathcal{L}_H = T_{2,2} = \widehat{\sigma_1^2}$ ([`def:hopf-diquark`](#def:hopf-diquark)) has **vanishing hyperbolic volume**, $\mathrm{Vol}(\mathcal{L}_H)=0$. This describes a volume-less correlation. Two molecules link without bonding. They share no bonded volume. This provides the topological home of **dispersion** (the van der Waals force): attraction without a chemical bond. Within this Hopf channel, the symmetric $e_+$ block is the retained $[2]_q$ / diquark carrier. The van der Waals force itself is **not** $e_+$. It is the **bar-odd residual** $\sinh(2\lambda)(e_+-e_-)$ that the canonical $P_{\mathrm{avg}}$ projection discards ([`prop:vdw-pskew-isolation`](#prop:vdw-pskew-isolation)). The dispersion force is an explicit (small, discarded) object, not an unmodelled residual.

The block is a genuine Wedderburn projector: $e_+ + e_- = 1$ and $e_+^2 = e_+$ (Lean `blocks_partition_unity`, `vdw_idempotent_cleared`; both sorry-free in Lean 4.24.0 + Mathlib). The Hopf link is *not* a separate operator from $e_\pm$. In $H_2(q)$, $\sigma_1^2 = (q-q^{-1})\sigma_1 + 1$ is algebraically dependent on $\{1,\sigma_1\}$. The operator-selection SDP over $\{1,\sigma_1,\sigma_1^2\}$ is rank-deficient. The independent blocks are exactly $e_+$ (the symmetric / Hopf-diquark carrier) and $e_-$ (the antisymmetric / directional block). Van der Waals is the **bar-odd** combination $\sinh(2\lambda)(e_+-e_-)$ of these two blocks, not either block alone.
<!-- FILE_END: van-der-waals-hopf-channel.md -->

<!-- FILE_START: hopf-link-symmetric-decomposition.md -->
*Lean sibling: a field $R$ carrying the $q$-data (AGENTS.md §7c); the identity is purely algebraic modulo the Hecke relation.*

**Proposition (Hopf-link symmetric decomposition).** *The Hopf element $\sigma_1^2$ of $H_2(q)$ weights the two blocks of [`def:van-der-waals-hopf-channel`](#def:van-der-waals-hopf-channel) by the squared block eigenvalues:*

$$
  \sigma_1^2 = q^2 e_+ + q^{-2} e_-.
$$

*Equivalently, cleared of the $[2]_q = q+q^{-1}$ denominator:*

$$
  [2]_q \sigma_1^2 = q^2 (\sigma_1+q^{-1}) + q^{-2} (q-\sigma_1).
$$

*This follows from the Hecke relation $\sigma_1^2 = (q-q^{-1})\sigma_1 + 1$ (Lean `hopf_symmetric_decomposition`, sorry-free, verified Lean 4.24.0).*

The Hopf element $\sigma_1^2$ ([`prop:trm-hopf-sigma1-sq-closed-form`](#prop:trm-hopf-sigma1-sq-closed-form)) splits between the symmetric $e_+$ and antisymmetric $e_-$ blocks. At $q_0$, the symmetric weight fraction is $q^2/(q^2+q^{-2}) \approx :val[vdw_sigma1sq_pct_symmetric]{precision=1, witness=computations/hbond-vdw-sdp.witness.json}\%$. This $\approx 60/40$ split is not dominant. The van der Waals force does not correspond to the $e_+$ block. It corresponds to the bar-odd residual $\sinh(2\lambda)(e_+-e_-)$ that the canonical $P_{\mathrm{avg}}$ projection discards (`prop:vdw-pskew-isolation`). The symmetric block $e_+$ (Markov $q$-dimension $\approx :val[vdw_e_plus_qdim]{precision=3, witness=computations/hbond-vdw-sdp.witness.json}$) is the retained $\cosh$ carrier, distinct from the antisymmetric block $e_-$ ($q$-dimension $\approx 0.304$). Neither block alone constitutes van der Waals.

This completes the structural identification. The molecular dispersion energy scale poses a separate archimedean (inter-molecular-separation) question. The bare $e_+$ resides at the $\hbar_q$-scale. This Hecke decomposition does not fix the long-distance suppression to the $\sim 0.5\,\mathrm{kJ/mol}$ molecular van der Waals energy.
<!-- FILE_END: hopf-link-symmetric-decomposition.md -->

<!-- FILE_START: vdw-pskew-isolation.md -->
*Lean sibling: any commutative ring with formal $q, q_i$ (fibre-level, no reality imposed — the `alpha-em-habiro-bar-involution` convention; AGENTS.md §7c).*

**Proposition (van der Waals $=$ the bar-odd $P_{\mathrm{skew}}$ channel).**
*Under the bar involution $q \mapsto q^{-1}$, the Hopf weighting of [`prop:hopf-link-symmetric-decomposition`](#prop:hopf-link-symmetric-decomposition) splits into a bar-even and a bar-odd part. With rapidity $\lambda = \ln q$:*

$$
  2\,\sigma_1^2 \;=\;
  \underbrace{2\cosh(2\lambda)\,\mathbf 1}_{\text{bar-even (retained)}}
  \;+\;
  \underbrace{2\sinh(2\lambda)\,(e_+ - e_-)}_{\text{bar-odd } (P_{\mathrm{skew}})}.
$$

*This uses the identities $q^2+q^{-2}=2\cosh 2\lambda$, $q^2-q^{-2}=2\sinh 2\lambda$, and $e_+ + e_- = \mathbf 1$.*
<!-- FILE_END: vdw-pskew-isolation.md -->

<!-- FILE_START: vdw-pskew-isolation-interpretation.md -->
**Van der Waals is the bar-odd residual** $\sinh(2\lambda)\,(e_+-e_-)$. Per [`crossing-energy-decomposition`](#prop:crossing-energy-decomposition), the $\sinh$ channel represents the antisymmetric Coulomb–EM channel. The canonical $P_{\mathrm{avg}}$ projection ([`def:bar-involution`](#def:bar-involution)) **discards** it. This explains why the van der Waals force is small (a discarded residual), suppressed by $\sinh$ or $h$-powers rather than carrying covalent-scale energy, and absent from the main mass/binding formula. The retained bar-even part is the trivial $\cosh(2\lambda)\,\mathbf 1$ carrier (the "hidden cosh"). This retained part is not the van der Waals energy itself.

**Im(q) caveat.** Per [`rem-im-q-vs-p-skew`](#rem:im-q-vs-p-skew), the $P_{\mathrm{skew}}$ ($\sinh$) content is **real** at real $q$. It is kept then discarded, not imaginary. $\mathrm{Im}(q)$ operates as a separate lever, set to zero by convention. The van der Waals residual is a real observable residing in the discarded sector. A non-zero $\mathrm{Im}(q)$ would constitute a distinct, later refinement, entirely separate from this channel.

**$\alpha_{EM}$ occupies the same Hopf channel.** The fine-structure constant acts as a 2-strand Hopf-operation coupling. By [`thm:em-spectral-completeness`](#thm:em-spectral-completeness), the 2-strand braiding possesses exactly the two idempotents $e_+, e_-$. Combining [`cor:gauge-coupling-uniqueness`](#cor:gauge-coupling-uniqueness) and [`prop:alpha-em-categorical-trace-ratio`](#prop:alpha-em-categorical-trace-ratio) establishes $\alpha_{EM}$ as the unique multiple of the **antisymmetric $e_-$** coupling: $\alpha_{EM} = h^2/(q\,\delta_q(T_{2,9})\delta_q(T_{3,5}))$, with $\delta_q(T_{2,k}) = q^k - q^{-k} = h\,[k]_q$ (the $\sinh$/$e_-$ trace). Therefore, $\alpha_{EM}$ (the $e_-$ coupling) and the van der Waals force (the bar-odd $\sinh(2\lambda)(e_+-e_-)$ residual) constitute the **same antisymmetric $\sinh$/EM channel** of the Hopf $H_2(q)$ operation. The fine-structure constant and the dispersion force represent two faces of a single Hopf knot operation. The $\alpha_{EM}$ Habiro element [`prop:alpha-em-habiro-bar-involution`](#prop:alpha-em-habiro-bar-involution), given by $H = [2]_q(1-h^2\alpha) = 2\cosh\lambda\,(1-h^2\alpha)$, is the **bar-even** next-order correction (a $\cosh$ carrier multiplied by a $\sinh^2$ correction). This sits opposite the bar-odd van der Waals term.

At $q_0$: $\cosh(2\lambda) \approx :val[vdw_cosh_2lambda]{precision=5, witness=computations/vdw-pskew-sinh-probe.witness.json}$. The bar-odd residual evaluates exactly to $\sinh(2\lambda)(e_+-e_-) \approx :val[vdw_bar_odd_residual]{precision=5, witness=computations/vdw-pskew-sinh-probe.witness.json}$ (no fit).

## Narrowed probe

This formally prunes the search space. The molecular van der Waals energy emerges as the archimedean projection of the **exact** bar-odd expression $\sinh(2\lambda)\,(e_+-e_-)$. It is neither an $h^k$ fit nor a $\cosh$ factor on the covalent ladder. The one remaining open piece is the archimedean inter-molecular separation ($1/r^6$, where $e_+$ represents the touching limit). This spatial term scales the fibre residual to the observed $\sim\!\mathrm{kJ/mol}$ molecular energy. This scaling remains open, not fitted.

## Lean structure

The file `QOU.VdwPskew` (sibling `vdw-pskew-isolation.lean`) formalises these results. It contains `hopf_bar_even_odd_decomposition` (the pure-`ring` bar split) and `vdw_is_bar_odd_residual` (the bar-odd part isolated on the idempotents). Both are sorry-free and verified in Lean 4.24.0 with Mathlib.
<!-- FILE_END: vdw-pskew-isolation-interpretation.md -->

<!-- FILE_START: molecular-hbond-phase-transition.md -->
We fix the critical temperatures of [`prop:phase-transition-boundary`](#prop:phase-transition-boundary) using the $S^3$-boundary action $\mathfrak{S}_q^{(\partial)}$. For a molecular liquid, this boundary action admits an explicit braid realization: it represents the hydrogen-bond network cohesion. This cohesion is gated by the discrete $\mathrm{sp}^3 \leftrightarrow \mathrm{pure}\text{-}p$ flip that sets the bond angle.

**The hydrogen bond as an $h^2$-suppressed crossing.** 
A covalent $X$–$H$ bond is a $\sigma$-crossing (the shared trefoil, [`covalent-bond-shared-trefoil`](#def:covalent-bond-shared-trefoil)). A hydrogen bond $X\!-\!H\cdots Y$ is the weak inter-molecular crossing between the donor $\sigma$ and the acceptor lone pair. It is suppressed by the square of the substrate $q$-deformation parameter $h = q_0 - q_0^{-1}$:

$$
  E_{\mathrm{HB}} = h^2 E_{\mathrm{cov}}, \qquad h^2 \approx :val[hbond_h_squared]{precision=4, witness=computations/hbond-categorical-action.witness.json}.
$$

The substrate $q_0$ entirely fixes this $h^2$ suppression. It matches the measured hydrogen-bond to covalent energy ratio ($\approx 0.044$, or $\approx 20$ vs $\approx 460\ \mathrm{kJ/mol}$ for water). The boundary action is the sum over the molecule's net hydrogen bonds:

$$
  \mathfrak{S}_q^{(\partial)} = n_{\mathrm{HB}} h^2 E_{\mathrm{cov}},
$$

where $n_{\mathrm{HB}}$ is the net hydrogen-bond count derived from the braid/VSEPR lone-pair structure ([`tetrahedral-hbond-directions`](#prop:tetrahedral-hbond-directions)).

**The $\mathrm{sp}^3$ gate.** 
A directional hydrogen bond requires a directional ($\mathrm{sp}^3$) acceptor lone pair. Thus, $\mathfrak{S}_q^{(\partial)}$ is gated by the same discrete $\mathrm{sp}^3 \leftrightarrow \mathrm{pure}\text{-}p$ flip that establishes the bond-angle base ([`prop:symmetric-block-domain-weight`](#prop:symmetric-block-domain-weight); penetration gap $\Delta(n)\propto(n-1)$, flip at $n=2\to 3$). Period-2 atoms are $\mathrm{sp}^3$ and form hydrogen bonds. Period-3+ atoms are $\mathrm{pure}\text{-}p$ and do not. The mechanism that opens the H–O–H angle is identical to the mechanism that elevates the boiling point of water.

**Boiling and freezing.** 
We compute the boiling temperature $T_q^{(g\to l)} = \mathfrak{S}_q^{(\partial)}/[2]_q$. The entropy of vaporisation is the pure $q$-number $[2]_q = q+q^{-1}$. The latent heat $L = \mathfrak{S}_q^{(\partial)}$ follows with no free parameters:

| | $n_{\mathrm{HB}}$ | $\mathrm{sp}^3$? | $L^{\mathrm{pred}}$ (kJ/mol) | $L^{\mathrm{obs}}$ | tier |
|---|---|---|---|---|---|
| $\mathrm{H_2O}$ | $2$ | yes | $:val[hbond_h2o_L_pred]{precision=1, witness=computations/hbond-categorical-action.witness.json}$ | $40.7$ | near-match ($:val[hbond_h2o_err_pct]{precision=1, witness=computations/hbond-categorical-action.witness.json}$) |
| $\mathrm{HF}$ | $1$ | yes | $24.7$ | $25.2$ | near-match ($1.9\%$) |
| $\mathrm{H_2S}$ | $-$ | no ($\mathrm{pure}\text{-}p$) | $0$ (H-bond off) | $18.7$ | dispersion |

The predicted water latent heat falls within $\approx 1\%$ of the measured value. Using the bridge relation $k_B T_{\mathrm{phys}} = \hbar_q$ ([`boltzmann-constant`](#prop:boltzmann-constant)), we recover $T_{\mathrm{boil}}(\mathrm{H_2O}) \approx 369\ \mathrm{K}$ (observed $373\ \mathrm{K}$). The freezing point follows from $T_q^{(l\to s)} = \mathfrak{S}_q^{(\partial)}/([2]_q[n_K]_q)$, yielding the ratio $T_{\mathrm{melt}}/T_{\mathrm{boil}} = 1/[n_K]_q$, where $n_K$ is the crossing number of the molecular knot.

*Observation structure.* We derive the $h^2$ suppression and the $\mathrm{sp}^3$ gate from the substrate and the bond-angle flip. We input the covalent $E_{\mathrm{cov}}$ and the latent heat $L^{\mathrm{obs}}$ from experiment. The dispersion latent heat of the non-hydrogen-bonding ($\mathrm{pure}\text{-}p$) hydrides belongs to the Hopf channel ([`def:van-der-waals-hopf-channel`](#def:van-der-waals-hopf-channel)) — the symmetric $e_+$ carrier. Proper van der Waals interactions correspond to the discarded bar-odd residual $\sinh(2\lambda)(e_+-e_-)$ of that channel (`prop:vdw-pskew-isolation`), which requires a separate mechanism.
<!-- FILE_END: molecular-hbond-phase-transition.md -->

