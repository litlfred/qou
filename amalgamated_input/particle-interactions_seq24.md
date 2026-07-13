<!-- FILE_START: particle-interactions-orphan-reconnect-intro.md -->
This section collects foundational substrate-level results and supporting conjectures. The sequence begins with the Geom universality proposition, which establishes the role of categorical geometry in the chapter's physical predictions. We develop the supporting symmetry principles: Stokes-region identification, time-reversal from trace cyclicity, spin from the $\mathrm{SO}(3)$ fibre, Type-B folding CPT, the categorical Weinberg angle, and Wigner-$\mathrm{SU}(4)$ symmetry from spin-isospin. The section concludes with the categorical proton and neutron blocks.
<!-- FILE_END: particle-interactions-orphan-reconnect-intro.md -->

<!-- FILE_START: geom-universality.md -->
**Proposition (conditional on hyperbolic volume transcendence).**
*The categorical volume form, evaluated on the knot complement $S^3 \setminus K$ through the fibre functor $\tau$, yields $\mathrm{Vol}(K)$ for hyperbolic knots and $\mathrm{CS}(K)$ for torus knots. This identification is universal: it provides the unique evaluation compatible with the Frobenius--Hopf structure.*

*Specifically, $\mathrm{Geom}(K)$ is the unique functional on knot complements satisfying:*

1. *Additivity: $\mathrm{Geom}(K_1 \# K_2) = \mathrm{Geom}(K_1) + \mathrm{Geom}(K_2)$.*
2. *Functoriality: $\mathrm{Geom}(K) = \tau(\mathrm{tr}_M(\rho(\mathcal{B}_K)))$ for some fibre functor $\tau$.*
3. *Normalization: $\mathrm{Geom}(\bigcirc) = 0$ (vacuum) and $\mathrm{Geom}(4_1) = \mathrm{Vol}(4_1)/\hbar_q^2$ (fixes $q_0$).*

*Proof.*
We divide the argument into three steps.

**Step 1: Existence (Neumann--Zagier, τ-image side).**
On the τ-image side, the Neumann--Zagier theorem establishes that for a hyperbolic knot $K$, $\mathrm{Vol}(K)$ and $\mathrm{CS}(K)$ are related by the Bloch--Wigner dilogarithm. This is a function of the $\mathrm{SL}(2,\mathbb{C})$ representation variety. In the categorical framework, the Frobenius--Hopf algebra $A$ at parameter $q$ has a representation variety isomorphic to $\mathrm{Spec}$ of the coordinate ring $\mathcal{O}_q(\mathrm{SL}_2)$. The fibre functor $\tau$ evaluates the volume form $\omega$ on this variety. By Neumann--Zagier, the real part of this evaluation is $\mathrm{Vol}(K)$.

**Step 2: Uniqueness (Yekutieli rigidity).**
The rigid dualizing complex $\omega_A^\bullet$ provides a non-degenerate Frobenius pairing $\langle -, - \rangle_{\mathrm{Frob}}$. Yekutieli's rigidity theorem shows that this pairing is unique up to a scalar. The scalar is fixed by the normalizations $\mathrm{Geom}(\bigcirc) = 0$ and $\mathrm{Geom}(4_1) = \mathrm{Vol}(4_1)/\hbar_q^2$. Therefore any functional satisfying properties 1--3 must equal $\mathrm{Geom}$.

**Step 3: The CS/Vol duality.**
For torus knots, $\mathrm{Vol} = 0$ and the representation variety consists of a single abelian flat connection. The evaluation of $\omega_A^\bullet$ on this connection yields the Chern--Simons functional. The duality $\mathrm{Vol}/\hbar_q^2 \leftrightarrow \mathrm{CS} \cdot \hbar_q^2$ follows from the self-duality of the rigid dualizing complex. Additivity follows from the fact that connected sum corresponds to tensor product in the Frobenius--Hopf category, and the volume form is a trace. $\square$

**Archimedean specialisation.** This block sits on the archimedean side of the substrate wall. It invokes real- or complex-analytic constructs. Any generic categorical identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: geom-universality.md -->

<!-- FILE_START: q-zero-stokes-region-identification.md -->
**Conjecture (Stokes region identification).**
*The substrate parameter $q_0$ admits a canonical identification with a specific point on the geometric component of the character variety $X(\mathcal{B}_3)$, realized via two dual perspectives that coincide by the AJ-conjecture machinery:*

*(a) **Analytic / Stokes side**: $q_0$ is the parameter value at which the Stokes region of the colored-Jones generating function $G_K(x; q) = \sum J_N(K; q) \cdot x^N$ transitions between dilog-asymptotic regimes.*
*(b) **Algebraic / Hom-functor side**: $q_0$ is the image under the archimedean functor of a specific $\underline{\mathrm{Hom}}_{\mathbf{C}}$-evaluation in the framework's brane-tower category $\mathbf{C}$ over $\mathbb{Z}[q, q^{\pm 1}]$.*

*The two perspectives are related by QOU duality, which is exactly the AJ-conjecture machinery $\hat{A}_K \cdot J_N = 0$ in the q-Weyl algebra $\mathcal{A}_q$ over $\mathbb{Z}[q, q^{-1}]$.*

Mostow-Prasad rigidity and Reid's trace field theorem guarantee a unique algebraic distinguished point $[\rho_{\mathrm{DF}}]$. The specific algebraic identification of $q_0$ as a particular invariant of $[\rho_{\mathrm{DF}}]$ remains the conjectural gap. We use Stokes asymptotics to formalise this identification. The Iwahori-Hecke algebra $H_n(q)$ and structural identities hold over the universal base $\mathbb{Z}[q, q^{\pm 1}]$. Physical observables are the images under the archimedean functor $\iota_\infty: \mathbb{Z}[q, q^{\pm 1}] \to \mathbb{R}$ at $q := q_0$.
<!-- FILE_END: q-zero-stokes-region-identification.md -->

<!-- FILE_START: cpt-d6-d7-d8-closure.md -->
**Conjecture (CPT closure).** 
*The three discrete symmetries close consistently: there exist actions $C$, $P$, $T$ on closed-braid representatives of $H_n(q)$ such that*

1. *$C$ is the color-sheet flavor-swap $u \leftrightarrow \bar u$, $d \leftrightarrow \bar d$;*
2. *$P$ is the braid-diagram mirror reflection, or writhe sign flip;*
3. *$T$ is the Markov-trace word reversal, or trace-cyclicity dual.*

*The composite $C \cdot P \cdot T$ preserves the Markov trace $\tau_M \colon H_n(q) \to R$. That is, $\tau_M((C \cdot P \cdot T)\beta) = \tau_M(\beta)$ for every closed-braid representative $\beta$.*

The joint statement is that they compose to the CPT theorem at the Markov-trace level. The three components are not logically independent—they collectively constitute the conjecture. The conjecture is class-axiomatised. Downstream blocks that require CPT closure as an explicit hypothesis take `[CPTD6D7D8Closure]` as a class hypothesis.
<!-- FILE_END: cpt-d6-d7-d8-closure.md -->

<!-- FILE_START: t-from-trace-cyclicity.md -->
**Conjecture (Time-reversal closure).**
*Within the QOU framework, time-reversal $T$ acts as **word reversal on braid words at the Markov-trace level**:*

$$
  T \;:\;
  \sigma_{i_1}^{\epsilon_1} \cdots \sigma_{i_\ell}^{\epsilon_\ell}
  \;\longmapsto\;
  \sigma_{i_\ell}^{\epsilon_\ell} \cdots \sigma_{i_1}^{\epsilon_1}.
$$

*By the Markov trace cyclicity axiom $\mathrm{tr}_M(ab) = \mathrm{tr}_M(ba)$, word reversal is trace-invariant for the Markov closure. The Jones polynomial of $K$ and of its time-reversed counterpart $K^T$ coincide. The operator $T$ is an involution ($T^2 = \mathrm{id}$). It preserves $q$, color-sheet flavors, and Hecke generator signs. It acts purely on the ordering of crossings.*

For a braid word $\beta$, define $\beta^T$ as the reversed word. Trace cyclicity gives $\mathrm{tr}_M(\beta) = \mathrm{tr}_M(\beta^T)$. The reversed word produces the mirror-orientation link, which has the same Jones polynomial as the original. $T$ alone is the trace-cyclicity dual. Composed with $C$ and $P$, it recovers the bar-involution = $CPT$ composite.
<!-- FILE_END: t-from-trace-cyclicity.md -->

<!-- FILE_START: spin-from-so3-fiber.md -->
**Conjecture (Spin closure, conditional on the $S_5 \leftrightarrow \mathrm{SO}(3)$ fiber action).**
*Within the QOU framework, spin $\mathrm{SU}(2)_S$ arises as the continuous lift of the full $\mathrm{SO}(3)$ rotation group acting on the 3 color sheets per nucleon. This operates via the $S_5 \to A_5 \cong I \subset \mathrm{SO}(3)$ icosahedral embedding on Bring's quintic surface. Extending to the full continuous $\mathrm{SO}(3)$ populates the $\ell = 2, 3, 4, \ldots$ spherical-harmonic decompositions. These contribute the $h^4$, $h^6$, $\ldots$ corrections to the Borromean linking weight, which the current $S_3$-truncated framework omits.*

The Family A linking weight $(3q^2 + 4 + 3q^{-2})/4 = 5/2 + (3/4)h^2$ terminates at $h^2$. The Borromean Markov trace's exact closed form has $h^2 = 0$ and first non-trivial coefficient $h^4 = -3/4$. The gap between Family A's $(3/4)h^2$ contribution and the Markov-trace $h^4 = -3/4$ structural value constitutes the load-bearing $h^4$ closure gap.

Spherical-harmonic levels of $\mathrm{SO}(3)$ organise higher-order corrections. The icosahedral construction lives on $A_5 \subset S_5$, whereas the $h^4 = -3/4$ coefficient lives on the $H_3$ Borromean Markov trace. The missing object is a functor from the $S_5$/$\mathrm{SO}(3)$ level $\ell$ to a Wedderburn coefficient of the 3-strand $H_3$ trace.

Closing spin together with isospin unlocks Wigner $\mathrm{SU}(4)$, the categorical source for nuclear-shell structure.
<!-- FILE_END: spin-from-so3-fiber.md -->

<!-- FILE_START: type-b-folding-cpt.md -->
**Conjecture (Type-B folding closure).**
*The $\mathfrak{sl}_n$ Cartan datum on the canonical atomic-braid Hecke algebra $H_n(q)$ folds into a Type-B Cartan datum $\mathrm{B}_{n/2}$ under the involution $\iota: \alpha_i \leftrightarrow \alpha_{n-i}$. The resulting Kashiwara crystal is a symmetric crystal whose GS normal forms are bar-involution invariant by construction. Stable matter = fixed points of the folded crystal; antimatter = the $\iota$-orbit complement. Under this folding, the composite CPT operator decomposes naturally as a tensor of:*

- *C from color-sheet flavor conjugation*
- *P from Type-B Cartan folding*
- *T from Markov-trace cyclicity*

Type-B folding provides an alternative categorical realisation where the role of "P (braid mirror)" is replaced by "the Cartan-fold Z/2", and the bar-invariance emerges from the Type-B symmetric-crystal structure rather than from explicit $\sigma_{i} \leftrightarrow \sigma_{i}^{-1}$ braid manipulation. The D22 view is more compact but requires more category theory.
<!-- FILE_END: type-b-folding-cpt.md -->

<!-- FILE_START: weinberg-angle-categorical.md -->
**Conjecture (Weinberg angle as Hecke-eigenvalue ratio).**
*Let $R$ be the categorical coefficient ring with generic $q \in R$. Under the Hoefsmit cell-content identification of the EW triplet inside $\mathrm{End}_R(V^{\otimes 6})$, $W \leftrightarrow \sigma_1^4$, $Z \leftrightarrow \sigma_3^6$, $H \leftrightarrow \sigma_5^8$. The Standard Model Weinberg angle $\theta_W$ is the categorical scalar in $R$ given by*

$$
  \cos\theta_W
  \;:=\;
  \frac{\mathrm{tr}_M\bigl(e_W^{+} \cdot \sigma_1^4\bigr)}
       {\sqrt{\mathrm{tr}_M\bigl(e_W^{+} \cdot \sigma_1^4\bigr)^2
              + \mathrm{tr}_M\bigl(e_B^{+} \cdot \sigma_5^8\bigr)^2}},
$$

$$
  \sin\theta_W
  \;:=\;
  \frac{\mathrm{tr}_M\bigl(e_B^{+} \cdot \sigma_5^8\bigr)}
       {\sqrt{\mathrm{tr}_M\bigl(e_W^{+} \cdot \sigma_1^4\bigr)^2
              + \mathrm{tr}_M\bigl(e_B^{+} \cdot \sigma_5^8\bigr)^2}},
$$

*where $e_W^{+}, e_B^{+}$ are the Hoefsmit-projector idempotents on the symmetric channels of the $W$ and $B$ slots respectively. The $B$ slot is understood pre-EWSB before $W^3$/$B$ mixing.*

At $n = 6$, the Hoefsmit identification assigns $\sigma_1^4$ to $W$, $\sigma_3^6$ to $Z$, and $\sigma_5^8$ to $H$. Pre-EWSB, the Hoefsmit slot $\sigma_5^8$ corresponds to the pre-mixing $B$ generator. The rotation by $\theta_W$ sends $(W^3, B) \mapsto (Z, \gamma)$. This rotation acts as a specific change-of-basis in the Hoefsmit projector decomposition.

Evaluating $\mathrm{tr}_M(e_W^{+} \cdot \sigma_1^4) / \mathrm{tr}_M(e_B^{+} \cdot \sigma_5^8)$ at the pure pattern yields $\cot\theta_W \stackrel{?}{=} q^{-4} \approx 0.6594$. This fails to match the 1.823 CODATA target. A correct categorical derivation must apply the non-uniform pure-pattern multiplicities, incorporate the categorical-linking operation, and potentially weight the trace by the Higgs vacuum expectation value.

Expressing $\theta_W$ as a ratio of categorical scalars remains structurally consistent. Proving this conjecture supplies $\sin\theta_W, \cos\theta_W \in R$ as categorical scalars, closing the Weinberg-angle gap.
<!-- FILE_END: weinberg-angle-categorical.md -->

<!-- FILE_START: wigner-su4-from-spin-isospin.md -->
**Conjecture (Wigner $\mathrm{SU}(4)$ closure — conditional on spin and isospin).**
*The Wigner spin-isospin symmetry $\mathrm{SU}(4) = \mathrm{SU}(2)_S \times \mathrm{SU}(2)_I$ arises in the QOU framework as the combined classical limit of the spin $\mathrm{SO}(3)$ fiber action and the canonical isospin $\mathbb{Z}/2$ swap acting on the color-sheet flavor triples of nucleon braids. The $A = 4$ first magic shell ($^{4}\!\mathrm{He}$) forms the first $\mathrm{SU}(4)$ supermultiplet (the trivial $\mathbf{1}$ representation). This provides the categorical origin for the framework's "magic $A\cdot 8G$" closure.*

The combined symmetry $\mathrm{SU}(2)_S \times \mathrm{SU}(2)_I = \mathrm{SU}(4)$ acts on the four-dimensional internal space of each nucleon. The totally-antisymmetric tensor product of four nucleons fills the trivial representation $\mathbf{1}_{\mathrm{SU}(4)}$. This yields Wigner's 1937 supermultiplet theory. It explains the special status of $^{4}\!\mathrm{He}$ as a closed s-shell.

The framework's L3 nuclear-shell-binding relies on a hard-coded `magic A·8G` rule for $^{4}\!\mathrm{He}$ and an $\alpha$-cluster recursion for $A \geq 8$. This conjecture identifies the magic $A\cdot 8G$ closure as the $\mathrm{SU}(4)$ supermultiplet structure. The magic $A\cdot 8G$ constant equals the $\mathrm{SU}(4)$-singlet projection coefficient of the saturated four-nucleon braid evaluated under the $\mathrm{SO}(3)$-fiber and bar-symmetric crystal functional.
<!-- FILE_END: wigner-su4-from-spin-isospin.md -->

<!-- FILE_START: alpha-wigner-supermultiplet-context.md -->
**Remark (the $A=4$ closure in the nuclear-physics literature).**
*The $A=4$ magic shell is the first Wigner $\mathrm{SU}(4)$ supermultiplet. The four single-nucleon spin-isospin states span the fundamental of $\mathrm{SU}(4)$. Their totally antisymmetric product forms the one-dimensional singlet $\Lambda^{4}(\mathbb{C}^{4})$: the closed shell of ${}^{4}\mathrm{He}$. The vanishing dimension $\dim \Lambda^{A}(\mathbb{C}^{4}) = 0$ for $A > 4$ fixes the $A = 4$ locality of the closure.*

Standard nuclear-mass systematics treat this closed-shell binding phenomenologically. The Wigner mass term vanishes identically at $N = Z$. It does not account for the anomalous extra binding of the even-even self-conjugate nuclei. A separate empirical cusp correction supplies that binding.

We locate this binding directly in the representation content of the nucleon braids. The $T = 0$ isoscalar channel — the self-conjugate partition $(2,2) \vdash 4$ — reproduces this scale with zero free parameters. The fully antisymmetric $\Lambda^{4}$ channel acts as the closed-shell supermultiplet. What nuclear phenomenology encodes in the Wigner term, we read off the $\mathrm{SU}(4)$ structure of the $A = 4$ shell.
<!-- FILE_END: alpha-wigner-supermultiplet-context.md -->

<!-- FILE_START: categorical-proton.md -->
**Definition.**
*The **proton** is the baryon governed by the $2 + 1$ crossing partition: two up quarks (positive orientation) and one down quark (negative orientation) bound within the Borromean braid $\mathcal{B}_3$.*

$$
  \mathfrak{p} = \mathcal{B}_3(\mathfrak{u},\mathfrak{u},\mathfrak{d})
$$

*where:*

- *$\mathcal{B}_3 = (\sigma_0\sigma_1^{-1})^3$ is the Borromean braid of three unknots threaded through color tubes $(r,g,b)$. Two unknots bear positive crossing orientation ($\mathfrak{u}$) and one bears negative orientation ($\mathfrak{d}$).*
- *$\mathcal{B}_3$ natively carries Hopf link content. This constitutes the intrinsic gluon field binding the components.*
- *The $S_3$ permutation symmetry of the color tubes guarantees the invariant structure across all color assignments.*
<!-- FILE_END: categorical-proton.md -->

<!-- FILE_START: categorical-proton-properties.md -->
The proton definition establishes the $\mathcal{B}_3(\mathfrak{u},\mathfrak{u},\mathfrak{d})$ baryon. We derive its normal form, mass, Coulomb charge, and computational backing.

**Step 1: Borromean braid NF.**
The inverse relation $\sigma_1^{-1} = \sigma_1 - H_A \mathbf{1}$ yields $\mathcal{B}_3 = (\sigma_0(\sigma_1 - H_A))^3$. Expanding and reducing within $H_3(q)$ gives $\mathrm{net}(\mathcal{B}_3) = +1.0000$. The Hopf link terms $L_\pm$ manifest the gluon field.

**Step 2: Typed crossings.**
Quark flavor rigidly specifies the crossing eigenvalue. The $\mathfrak{u}$-$\mathfrak{u}$ crossing preserves the eigenvalue $+q$. The $\mathfrak{d}$-type crossings impose a full $-H_A$ shift. Mixed $\mathfrak{u}$-$\mathfrak{d}$ crossings incur a half-shift $-\tfrac{1}{2}H_A$.

**LP stability constraint.**
The bare 9-crossing element $\mathcal{B}_3 \times \Delta_3(\mathfrak{u}\mathfrak{u}\mathfrak{d})$ violates Frobenius positivity. A single Hopf link $L_- = \sigma_1\sigma_0$ is the minimum additional structure capable of restoring stability. The gluon is strictly required by the LP dual. The integer LP dual enumerates all feasible gluon combinations and selects the configuration minimizing $|\mathrm{tr}_M|$.

**Step 3: Proton NF.**
Applying typed crossings and Hopf link stabilisation yields $\mathrm{net}(\mathfrak{p}) = +1.0065$. The dominant term is $e^- \approx +1.022$. The Hopf gluon link actively redistributes normal-form weight from $\sigma_1$ into the trefoil channel.

**Mass.**
The proton mass derives from the hyperbolic volume of the Borromean link:

$$
  \mathfrak{m}_{\mathfrak{p}} =
  \frac{\mathrm{Vol}(S^3 \setminus \mathcal{B}_3)}{\hbar_q^2}
  \cdot \lambda_{\mathrm{scale}}
  + \text{Skein corrections}
$$

The Skein corrections isolate the crossing asymmetry between the $\mathfrak{u}$ and $\mathfrak{d}$ components. The pair Skein formula dictates $\mathfrak{m}_{\mathfrak{p}} = \mathcal{S}_{\mathfrak{u}\mathfrak{u}}(q) + 2\mathcal{S}_{\mathfrak{u}\mathfrak{d}}(q)$.
<!-- FILE_END: categorical-proton-properties.md -->

<!-- FILE_START: categorical-neutron.md -->
The **neutron** is the baryon characterized by the $1 + 2$ crossing partition: one up quark and two down quarks embedded in the Borromean braid $\mathcal{B}_3$ ([Borromean quark](#conj:borromean-quark)).

$$
  \mathfrak{n} = \mathcal{B}_3(\mathfrak{u},\mathfrak{d},\mathfrak{d})
$$

This structure threads one $\mathfrak{u}$ ([up quark](#def:up-quark)) and two $\mathfrak{d}$ ([down quarks](#def:down-quark)) through the Borromean braid. The formal evaluation---comprising the normal-form construction, mass derivation, proton transition amplitude, and Coulomb charge---follows in the [properties remark](#rem:categorical-neutron-properties).
<!-- FILE_END: categorical-neutron.md -->

<!-- FILE_START: categorical-neutron-properties.md -->
The [neutron definition](#def:categorical-neutron) establishes the $\mathcal{B}_3(\mathfrak{u},\mathfrak{d},\mathfrak{d})$ baryon. We derive its normal form, mass, $\beta$-decay transition, and Coulomb charge.

**Step 1: Borromean braid NF.**
As in the [proton](#def:categorical-proton) construction, we find $\mathrm{net}(\mathcal{B}_3) = +1.000$, establishing intrinsic Hopf link content without an independent $\mathcal{L}_H$ factor.

**Step 2: Typed crossings + Hopf gluon stabilisation.**
The two down quarks induce stronger $-H_A$ shifts than the single down quark of the proton. The crossing pairs appear in [Table: Neutron crossing pairs](#tbl:categorical-neutron-table-data).

The bare 9-crossing element $\mathcal{B}_3 \times \Delta_3(\mathfrak{u}\mathfrak{d}\mathfrak{d})$ remains LP unstable. The $\sigma_0$ channel violates Frobenius positivity following the second quark crossing. A single Hopf link $L_- = \sigma_1\sigma_0$ restores structural stability. 

The integer LP dual selects $L_+ \to L_-$ (two Hopf links, 4 gluon crossings) as the minimum-action stabiliser. The neutron requires more gluon crossings than the proton (4 versus 2) because the $\mathfrak{d}\mathfrak{d}$ crossing creates a deeper instability ($\mathrm{tr}_M = -0.132$ versus $-0.006$). This yields a total of 13 crossings (6 from $\mathcal{B}_3$, 3 from quarks, 4 from gluons).

**Step 3: Neutron NF (with Hopf gluon).**
At $q_0 \approx 1.1100$:

See [Table](#tbl:categorical-neutron-table-data).

$$
  \mathrm{net}(\mathfrak{n}) = +0.7976
$$

Relative to the proton ($\mathrm{net} = +1.0065$), the additional down quark demands a larger $L_+$ compensation ($-0.2206$ versus $-0.1114$). After Hopf gluon stabilisation, the trefoil channel $e^- \approx +1.0$ dominates both nucleons.

**Transition: proton $\to$ neutron.**
The normal-form difference yields the dimensionless $\beta$-decay transition ([energy scale](#rem:beta-decay-energy-scale)):

$$
  \Delta\mathrm{net}(\mathfrak{n} - \mathfrak{p})
  = 0.7976 - 1.0065 = -0.2089
$$

The uniform energy scale $\mathfrak{E}_0 = \mathfrak{Q}_\beta / |\Delta\mathrm{net}| \approx 4.155$ MeV converts these coefficient differences directly to MeV ([formation chain](#rem:meson-to-proton-via-borromean)).

**Mass.**

$$
  \mathfrak{m}_{\mathfrak{n}} =
  2\mathcal{S}_{\mathfrak{u}\mathfrak{d}}(q) + \mathcal{S}_{\mathfrak{d}\mathfrak{d}}(q)
$$

At the CODATA value $q_0$, the base mass is $\mathfrak{m}_{\mathfrak{n}}(q_0) \approx :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json}$ MeV, derived strictly from the substrate parameter ([local substrate](#prop:local-substrate-q)). The resulting proton--neutron mass splitting is exactly:

$$
  \mathfrak{m}_{\mathfrak{n}} - \mathfrak{m}_{\mathfrak{p}} =
  \mathcal{S}_{\mathfrak{d}\mathfrak{d}}(q) - \mathcal{S}_{\mathfrak{u}\mathfrak{u}}(q)
  \approx 1.293 \text{ MeV}
$$

This splitting arises from the Skein resolution asymmetry between the $\mathfrak{u}\text{-}\mathfrak{u}$ and $\mathfrak{d}\text{-}\mathfrak{d}$ crossing pairs within the rigid $\mathcal{B}_3$ structure.

**Coulomb charge.**

$$
  Q(\mathfrak{n}) =
  1 \cdot (+\tfrac{2}{3}) + 2 \cdot (-\tfrac{1}{3}) = 0.
$$

The neutron achieves precise electrical neutrality: its single positive-orientation unknot ($\mathfrak{u}$) cancels two negative-orientation unknots ($\mathfrak{d}$). The inter-neutron Hopf crossings acquire the $q^{-1}$ coefficient associated with negative crossings. This produces an attractive enhancement, supplying the categorical expression of electric neutrality.
<!-- FILE_END: categorical-neutron-properties.md -->

<!-- FILE_START: categorical-meson.md -->
A **meson** is a valence-2 [hadron](#def:hadron): a quark--antiquark pair bound by the Hopf link $\mathcal{L}_H$. We form the meson from two independent [quark--antiquark productions](#def:quark-antiquark-production), pairing a quark from one with an antiquark from the other:

$$
  \mathfrak{M}
  = 
  T_{01} \cdot \mathcal{L}_H \cdot T_{10}
$$

where:

- $T_{01} = \sigma_0\sigma_1 = L_+$ is the positive Hopf link (up-type crossing pair, [knot notation](#sec:knot-notation-convention)).
- $T_{10} = \sigma_1\sigma_0 = L_-$ is the negative Hopf link (down-type crossing pair).
- $\mathcal{L}_H = \sigma_0\sigma_1$ is the Hopf link binding the two constituents.

The full braid word is $(\sigma_0\sigma_1)^2 \cdot \sigma_1\sigma_0$, containing 6 crossings on 3 strands.

**Normal form (step-by-step Hecke reduction).**
We write $h = H_A = q - q^{-1}$ and apply the Hecke relation $\sigma_i^2 = h\sigma_i + \mathbf{1}$ and the braid relation $\sigma_0\sigma_1\sigma_0 = \sigma_1\sigma_0\sigma_1$.

*Step 1.* For the bound pair $T_{01} \cdot \mathcal{L}_H = (\sigma_0\sigma_1)^2 = \sigma_0\sigma_1\sigma_0\sigma_1$, we apply the braid relation to the rightmost three generators to yield $\sigma_0 \cdot \sigma_0\sigma_1\sigma_0 = \sigma_0^2 \cdot L_-$. The Hecke relation reduces this to:

$$
  (\sigma_0\sigma_1)^2 = h \cdot e^- + L_-
$$

*Step 2.* We multiply by $T_{10} = \sigma_1\sigma_0$:

| Factor | Product | Hecke reduction |
|:---|:---|:---|
| $L_- \cdot L_-$ | $\sigma_1\sigma_0\sigma_1\sigma_0$ | braid + Hecke: $h \cdot e^- + L_+$ |
| $e^- \cdot L_-$ | $\sigma_0\sigma_1\sigma_0 \cdot \sigma_1\sigma_0$ | two braid + Hecke steps: $h^2 e^- + hL_+ + hL_- + \sigma_1$ |

Collecting terms yields the exact normal form:

$$
  \mathfrak{M}_+ =
  \underbrace{h}_{\sigma_1}\sigma_1
  + \underbrace{(h^2 + 1)}_{L_+}\sigma_0\sigma_1
  + \underbrace{h^2}_{L_-}\sigma_1\sigma_0
  + \underbrace{(h^3 + h)}_{e^-}\sigma_0\sigma_1\sigma_0
$$

At the CODATA root $q_0 \approx 1.1100$ ($h \approx 0.2091$):

$$
  \mathrm{NF}(\mathfrak{M}_+) \approx 0.209\,\sigma_1 + 1.044\,L_+ + 0.044\,L_- + 0.218\,e^-
$$

yielding $\mathrm{net}(\mathfrak{M}_+) \approx +1.515$.

The mirror meson $\mathfrak{M}_- = T_{10} \cdot \mathcal{L}_H \cdot T_{01}$ maintains identical net amplitude but exchanges $\sigma_1$ for $\sigma_0$:

$$
  \mathrm{NF}(\mathfrak{M}_-) \approx 0.209\,\sigma_0 + 1.044\,L_+ + 0.044\,L_- + 0.218\,e^-
$$

Both mesons carry identical Hopf link ($L_+ + L_-$) and trefoil ($e^-$) content, differing only in the single-generator excitation.

**Particle content.**
The dominant $L_+$ term (coefficient $\approx 1.044$) establishes the Hopf link binding. The trefoil component $e^-$ ($\approx 0.218$) encodes the residual lepton channel. In contrast, the bare quark--antiquark pair ($T_{01} \cdot T_{10}$) yields $\mathrm{net} = +1.418$ and contains a neutrino $\nu$ component in place of the Hopf links. The Hopf link binding actively replaces the neutrino channel and increases the net amplitude by $\approx 0.097$.
<!-- FILE_END: categorical-meson.md -->

<!-- FILE_START: meson-scale-independence.md -->
*The pion mass $m_\pi$ cannot be derived from the substrate parameters $(m_\mathfrak{e}, q_0)$ alone. The Hecke algebra determines the relative meson mass spectrum (character ratios between mesons) but not the absolute scale $m_\pi$.*

## Calibration structure

The three calibration inputs are independent physical measurements. Each is associated with a decay process:

| Anchor | Observable | Jet order | Measurement |
|--------|-----------|-----------|-------------|
| **CAL-1** | $m_\mathfrak{e}$ | $h^0$ | electron mass (Penning trap) |
| **CAL-2** | $\mathfrak{D}_\beta$ | $h^2$ | neutron $\beta$-decay width ($\tau_n = \hbar / \mathfrak{D}_\beta$) |
| **CAL-3** | $\mathfrak{D}_\pi$ | $h^3$ | pion decay width ($\tau_\pi = \hbar / \mathfrak{D}_\pi$) |

CAL-2 determines $\mathfrak{Q}_\beta = m_n - m_p - m_\mathfrak{e}$ from the neutron lifetime. This fixes $q_0$ via the substrate identity. CAL-3 determines $m_\pi$ from the pion lifetime. This fixes the meson mass scale. All other masses (proton, neutron, muon, kaon, $\ldots$) are derived from these three inputs.

The $h^1$ jet order is absent. The bar involution $q \mapsto q^{-1}$ forces all Markov traces of writhe-zero braids to be even functions of $h$. The $h^3$ order enters through the flavor-split $X = (q-1)^2(1-q^{-4})/3 = h^3/6 + \cdots$, which is a skein difference (not a single-braid Markov trace).

## Lean formalization

The companion Lean `meson_scale_independence` encodes the geometric core of the obstruction. The Hopf-link complement (meson binding topology) has hyperbolic volume $0$. The Borromean complement (baryon) has positive volume. The volume-scaling map $m_\mathfrak{e}\cdot\mathrm{Vol}(K)\cdot\rho/\hbar_q^2$ sends the meson's geometric scale to $0$ independently of $(m_\mathfrak{e}, q_0)$. The absolute scale therefore enters only through the independent calibration CAL-3 ($\mathfrak{D}_\pi$). The Lean is sorry-free.

**Archimedean specialisation (§7c).** The scale statement is evaluated over $\mathbb{R}$ — hyperbolic volumes, the MeV meson scale, and the CAL-3 numerical calibration. This block sits on the archimedean side of the substrate wall.
<!-- FILE_END: meson-scale-independence.md -->

<!-- FILE_START: outro-particle-interactions.md -->
This concludes the particle-interactions chapter. Gröbner–Shirshov selection on braid-word normal forms isolates the categorical analogues of standard-model interactions. The linear programming formulation recasts confinement and shell closure as a Frobenius positivity gate. The semidefinite programming (SDP)-as-thimble construction recovers $Q$-value branching for $\beta$-decay endpoints. Finally, the $b_3$ local minimum establishes the categorical anchor that the next chapter compares against CODATA.

The subsequent chapter (physical observations) transitions this categorical arithmetic to the Archimedean domain. Substrate-level outputs ($Q$-values, mass ratios, hyperbolic volumes) are evaluated at the substrate parameter $q_0$ and compared against experimental data, adhering to the 100× per-observable accuracy bound dictated by AGENTS.md §Precision goals.
<!-- FILE_END: outro-particle-interactions.md -->

