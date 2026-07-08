<!-- FILE_START: electroweak-triplet-bring-embedding.md -->
*The even-twist 2-component torus links $T(2,4), T(2,6), T(2,8)$ — the braids $\sigma_1^{2k} \in B_2$ for $k = 2, 3, 4$ — have Seifert genera $1, 2, 3$ respectively. These genera strictly increase and satisfy $g \leq 4 = g(\Sigma_4)$. The three links therefore co-embed in the genus-$4$ Seifert fiber of Bring's surface alongside the saturating force-carriers $\{T(2,9), T(3,5)\}$. Moreover, the three cells carry the pairwise-orthogonal Hoefsmit idempotent decomposition in $\mathrm{End}_R(V^{\otimes 6})$.*

**Proof.**

The canonical Seifert surface of the 2-component torus link $T(2, 2k)$ has genus $g(T(2, 2k)) = k - 1$. At $k = 2, 3, 4$ the genera are $1, 2, 3$. These strictly increase and remain $\leq 4$. The even-twist links with genus in $\{1, 2, 3\}$ are exactly those with $k \in \{2, 3, 4\}$. The embeddability bound $g(K) \leq g(\Sigma_4) = 4$ places all three in the same genus-$4$ Seifert fiber alongside the saturating carriers.

The genus, enumeration, and embedding steps involve elementary $\mathbb{N}$-arithmetic. They are verified sorry-free in Lean. The Hoefsmit idempotent orthogonality is cited from the prior theorem. $\square$

**Scope.**
This proposition supplies the structural half of the electroweak torus-link story. It establishes that the triplet fits the genus-$4$ host. It does not fix which link carries $W^\pm$ versus $Z$ versus $H$. That physical identification constitutes the subsequent conjecture. This conjecture relies on the open selection, charge, and spin sub-conjectures.
<!-- FILE_END: electroweak-triplet-bring-embedding.md -->

<!-- FILE_START: electroweak-triplet-far-commuting-minimal.md -->
*Let $\sigma_a, \sigma_b, \sigma_c$ be pairwise far-commuting braid generators: $|a-b|, |b-c|, |a-c| \geq 2$. Then:*

1. *(Minimality.) These generators require at least $6$ strands. With $1 \leq a < b < c$, the pairwise gap $\geq 2$ forces $c \geq 5$, yielding $n \geq c+1 \geq 6$. The bound is attained uniquely by the consecutive odd triple $(a,b,c) = (1,3,5)$ in $B_6$.*
2. *(Enumeration.) The even-twist $2$-component torus links $T(2,2k)$ (braid $\sigma_1^{2k}$, Seifert genus $g = k-1$) with genus strictly between the trivial Hopf endpoint $g=0$ and the genus-$4$ Bring saturation ($1 \leq g \leq 3$) are exactly those with $k \in \{2,3,4\}$: the triplet $T(2,4), T(2,6), T(2,8)$.*

This forms the mathematical core of the electroweak selection principle C1. Both halves rely on elementary $\mathbb{N}$-arithmetic and are verified sorry-free in Lean.

**Far-commuting minimality.**

Each even-twist carrier $T(2,2k)$ acts on a single strand-pair. Three mutually non-interfering carriers require three generators $\sigma_a, \sigma_b, \sigma_c$ that pairwise commute without sharing a strand. This is the far-commutativity condition $|i-j| \geq 2$. In $B_n$, a generator $\sigma_i$ requires $1 \leq i \leq n-1$. Three indices with $a \geq 1$, $b \geq a+2$, $c \geq b+2$ dictate $c \geq 5$, so $n = c+1 \geq 6$. Setting $c = 5$ forces $(a,b,c) = (1,3,5)$. The $n=6$ minimum supplies three disjoint strand-pairs $\{1,2\}, \{3,4\}, \{5,6\}$ carrying $\sigma_1^4, \sigma_3^6, \sigma_5^8$.

**Enumeration.**

The genus filtration places the trivial Hopf link $T(2,2)$ at $g=0$ and the force-carrier saturation $\{T(2,9), T(3,5)\}$ at $g=4 = g(\Sigma_4)$. The open window $0 < g < 4$ contains exactly the genera $1,2,3$ ($k \in \{2,3,4\}$). This forward inclusion matches the arithmetic proved sorry-free.

**Scope.**

This theorem elevates the mathematical content of C1 to a proved statement. It does not assert that the electroweak sector is this set of links. That identification remains a conjectural input. The far-commuting bound and enumeration provide the facts upon which that postulate operates.
<!-- FILE_END: electroweak-triplet-far-commuting-minimal.md -->

<!-- FILE_START: electroweak-higgs-torus-link-triplet.md -->
**Conjecture (electroweak/Higgs torus-link identification).**
*In any QOU built on Bring's surface with EM/strong sector $\{T_{2,9}, T_{3,5}\}$, the standard-model electroweak gauge bosons $W^\pm, Z$ and the Higgs scalar $H$ correspond to the three even-twist $2$-component torus links of the sub-saturating complement:*

$$
  W^{\pm} \;\longleftrightarrow\; T(2,4),
  \qquad
  Z \;\longleftrightarrow\; T(2,6),
  \qquad
  H \;\longleftrightarrow\; T(2,8).
$$

This is the top node of the electroweak conjecture lattice. Its provable base — that these three links exist, have Seifert genera $1, 2, 3$, co-embed in Bring's genus-$4$ fiber alongside the saturating carriers, and fit minimally in $B_6$ at the far-commuting triple $(1,3,5)$ — is verified sorry-free. What remains conjectural is the identification itself. Charge and spin are proved consequences of a single sector postulate.

**The conjecture lattice (narrowed).**

| Node | Kind | Rests on | Content |
|------|------|----------|---------|
| **C1** selection | primary | — | EW carriers are the nontrivial, strictly sub-saturating even-twist links ($0 < g < 4$). |
| **C2** enumeration | dependent (C1) | C1 | These carriers are exactly $\{T(2,4), T(2,6), T(2,8)\}$. |
| **C$_{	ext{sector}}$** sector assignment | primary | — | Which link sits in the singlet $A_+$ versus doublet $A_-$ of the spin involution. |
| **C$_{	ext{top}}$** identification | dependent (C1, C$_{	ext{sector}}$) | C1, C$_{	ext{sector}}$ | The full map above. |

The former C3 (charge) and C4 (spin) are proved consequences of C$_{	ext{sector}}$.

**C1 — the selection principle.**

The electroweak carriers are the nontrivial, strictly sub-saturating even-twist $2$-component torus links. Their Seifert genus $g$ lies in the window $0 < g < 4 = g(\Sigma_4)$. This forms the sub-saturating complement of the genus-$4$ saturating force-carrier knots $\{T_{2,9}, T_{3,5}\}$. These two are the only coprime solutions of $(p-1)(q-1) = 8$, exhausting Bring's genus-$4$ capacity. The Hopf link $T(2,2)$ (genus $0$) is the trivial endpoint and is excluded. The saturation mechanism that forces $\{T_{2,9}, T_{3,5}\}$ for the strong carriers selects the sub-saturating window for the weak carriers.

**C2 — enumeration.**

Given C1, the carrier window $0 < g < 4$ contains exactly the genera $1, 2, 3$ ($k \in \{2, 3, 4\}$): the triplet $T(2,4), T(2,6), T(2,8)$. The forward inclusion is a provable enumeration. The conjectural content of C2 is the reverse inclusion: all three genera are realised as carriers.

**C$_{	ext{sector}}$ — the single sector-assignment postulate.**

Charge and spin are unified by one $\mathbb{Z}/2$ datum: the assignment of each carrier to a sector of the spin involution $\sigma$, $A = A_+ \oplus A_-$. Restricted to the sym/alt Hecke block, $\sigma$ is the swap of the eigenvalues $q^{2k} \leftrightarrow q^{-2k}$. Its projections give a bar-even part in $A_+$ (neutral, retained by the Markov trace) and a bar-odd part in $A_-$ (charged, traceless). The Higgs is the bar-even self-dual carrier.

Given the sector assignment ($H$ singlet, $W^\pm, Z$ doublets), spin and charge follow. $H \in A_+$ implies scalar (spin $0$) and neutral. $W^\pm \in A_-$ implies vector (spin $1$) with $T_3 = \pm 1$. $Z \in A_-$ implies vector, neutral with $T_3 = 0$ via the $(W^3, B) \mapsto (Z, \gamma)$ Weinberg mixing. The remaining conjectural input is the sector assignment itself.

**The $\sigma_5^8$ bar-grading is derived from spin.**

The Weinberg-angle block reads the Hoefsmit slot $\sigma_5^8$ as the $\mathrm{U}(1)_Y$ hypercharge gauge boson $B$. This block reads $\sigma_5^8$ ($= T(2,8)$, strands $5$–$6$) as the Higgs. There is no conflict: $\sigma_5^8$ carries both, bar-graded by the spin involution. The Higgs boson $H$ is the $A_+$ (bar-even, scalar) part. The hypercharge gauge boson $B$ is the $A_-$ (bar-odd, vector) part.

This bar-grading is derived from the two carriers' spins. The sector$	o$spin map is injective and inverts. Spin determines the sector. The Higgs is a scalar and $B$ a vector as independent physical inputs, so $H \in A_+$ and $B \in A_-$ are forced. The residual postulate is that both $H$ and $B$ inhabit the one $\sigma_5^8$ slot. The self-dual figure-eight $4_1$ is the Higgs mass mechanism, not the $125\,$GeV Higgs boson. The boson is the electroweak-slot link $T(2,8) = A_+$ of $\sigma_5^8$.

**The $W$ vs $Z$ slot assignment is a free label.**

Spin fixes each carrier's sector (scalar $H 	o A_+$; vectors $W, Z 	o A_-$). It does not fix which of the two $A_-$ vector slots is the charged $W^\pm$ and which is the neutral $Z$. The corpus map $Q = 	frac12\,\mathrm{writhe}$ on the all-positive braid $\sigma_1^{2k}$ gives $Q(T(2,2k)) = k > 0$ for all three carriers. It cannot single out the neutral slot. The assignment $W = \sigma_1^4$ relies on the mass ordering $4 < 6 < 8$. Both $W = \sigma_1^4$ and the mirror $W = \sigma_3^6$ satisfy every proved constraint.

**Supporting evidence.**

1. **Mass ordering.** The standard-model ordering $m_{W^\pm} < m_Z < m_H$ maps monotonically onto the crossing-number ordering $4 < 6 < 8$.
2. **PSD-feasibility probe.** An exploratory SDP-feasibility probe shows PSD discrimination. Only the even-twist torus-link triplet $\{T(2,4), T(2,6), T(2,8)\}$ produced positive-semidefinite Hecke certificates on every Wedderburn block. 

PSD-feasibility is necessary but not sufficient. It holds for every even-twist $T(2, 2k)$ at any $k \geq 1$.

**What the conjecture closes.**

If true, the identification supplies the categorical structure for the weak-scale crossing count $N_v$ in the Fermi-constant decomposition $G_F = 1/(\sqrt{2}\,v^2)$, $v = N_v\,E_	imes\,\mu_0$. The residual to close is C1 (selection) and C$_{	ext{sector}}$ (sector assignment).
<!-- FILE_END: electroweak-higgs-torus-link-triplet.md -->

<!-- FILE_START: electroweak-triplet-charge-spin-from-involution.md -->
**Theorem (conditional on the electroweak sector-selection postulate).**
*Fix the categorical coefficient ring $R$ (a field with $	frac{1}{2} \in R$) and the sector-selection postulate: each electroweak carrier is assigned to the spin-singlet sector $A_+$ ($\sigma$-fixed, bar-even) or the spin-doublet sector $A_-$ ($\sigma$-negated, bar-odd) of the spin involution $\sigma$, with $H$ the singlet and $W^\pm, Z$ the doublets, together with the isospin label map $T_3(W^\pm) = \pm 1$, $T_3(Z) = T_3(H) = 0$. Then the spin and charge of the triplet are determined:*

$$
  \mathrm{spin}(H) = 0 \ (	ext{scalar, neutral}), \qquad
  \mathrm{spin}(W^\pm) = \mathrm{spin}(Z) = 1 \ (	ext{vector}),
$$
$$
  T_3(W^\pm) = \pm 1 \ (	ext{charged}), \qquad T_3(Z) = 0 \ (	ext{neutral}).
$$

Charge and spin are not independent open conjectures. Both follow from one physics selection postulate through the corpus spin involution. This collapses the former C3 (charge) and C4 (spin) into proved consequences.

**The provable half — bar-parity of the even-twist carriers.**

The even-twist carrier $T(2,2k)$ occupies the two-dimensional sym/alt Hecke block with eigenvalues $(q^{2k}, q^{-2k})$. The spin involution acts on this block as the swap $\sigma(x,y) = (y,x)$. This is precisely the bar involution $q \mapsto q^{-1}$ sending $q^{2k} \leftrightarrow q^{-2k}$. Its projections split the carrier:

1. **bar-even part** $a_+ \in A_+$, $\sigma$-fixed, with neutral (Markov-trace) value $q^{2k} + q^{-2k}$.
2. **bar-odd part** $a_- \in A_-$, $\sigma$-negated, traceless with nonzero skew value $q^{2k} - q^{-2k}$.

The Higgs is the bar-even / self-dual / real-volume carrier. The $W^\pm, Z$ are bar-odd.

**The forced quantum numbers.**

Given the sector assignment, spin is defined by $2s(c) = 0$ if $c$ is a singlet and $2s(c) = 2$ if $c$ is a doublet. Then $\mathrm{spin}(H) = 0$ (scalar) and $\mathrm{spin}(W^\pm) = \mathrm{spin}(Z) = 1$ (vector) are theorems. Neutrality is forced by bar-parity. A singlet carrier realises the bar-even part, a doublet the bar-odd part.

The genuinely postulated data are the sector map itself and the $T_3$ label. In particular $Z$ is a doublet (vector) yet neutral ($T_3 = 0$). Its neutrality is not bar-even membership but the $(W^3, B) \mapsto (Z, \gamma)$ Weinberg mixing.

**The $\sigma_5^8$ bar-grading is DERIVED from spin.**

The Weinberg-angle block reads the Hoefsmit slot $\sigma_5^8$ as the $\mathrm{U}(1)_Y$ hypercharge gauge boson $B$. The triplet block reads $\sigma_5^8$ ($= T(2,8)$, strands $5$–$6$) as the Higgs. There is no conflict: $\sigma_5^8$ carries both, bar-graded by the spin involution. The Higgs boson $H$ is the $A_+$ (bar-even, scalar) part. The hypercharge gauge boson $B$ is the $A_-$ (bar-odd, vector) part.

This bar-grading is derived from the two carriers' spins. The sector$	o$spin map is injective and inverts. Spin determines the sector. The Higgs is a scalar and $B$ is a vector as independent physical inputs, so $H \in A_+$ and $B \in A_-$ are forced. The residual postulate is that both $H$ and $B$ inhabit the one $\sigma_5^8$ slot.

**The $W$ vs $Z$ slot assignment is a free label.**

The sector membership $A_+ / A_-$ of each carrier is forced by its spin above. A charged carrier must be a bar-odd $A_-$ doublet. What is not forced is which of the two vector slots — $\sigma_1^4$ or $\sigma_3^6$ — hosts the charged $W^\pm$ versus the neutral $Z$. The corpus crossing$	o$charge map $Q = 	frac12\,\mathrm{writhe}$ on the all-positive braid $\sigma_1^{2k}$ gives $Q(T(2,2k)) = k > 0$ for every carrier. It cannot single out the neutral slot. The surviving $\mathrm{writhe} 	o I_3$ map assigns $2 I_3 = 2k$, nonzero on both vector slots. No proved crossing$	o$charge principle selects the $W$ slot. Both $W = \sigma_1^4$ and the mirror $W = \sigma_3^6$ satisfy every proved constraint.

**The signed charge-conjugation test.**

Charge conjugation is crossing reversal. The operation $C = (\sigma \leftrightarrow \sigma^{-1})$ reverses every crossing. A carrier is neutral iff it is a fixed point of $C$, i.e. $C$-invariant or amphichiral. Over $\mathbb{Z}$ this fixed-point condition is exactly the vanishing of the signed writhe.

Admitting the signed asymmetry does not force which slot is $W$. Two distinct signed labelings both satisfy the full $C$-invariance neutrality constraint yet disagree on the charged slot. The signed test constrains the neutral slot to be amphichiral, but not which slot it is.

The $C$-invariance criterion excludes every pure even-twist slot from being the neutral member. Each carrier $\sigma_1^{2k}$ has signed writhe $2k \neq 0$, so none is $C$-invariant. The neutral electroweak boson is necessarily not a single even-twist slot. It must be the mixed $(W^3, B) \mapsto (Z, \gamma)$ Weinberg combination.

**The two natural realizations of the second charge also fail.**

A hypothetical second baryon or color-trace charge nonzero on exactly one vector slot would determine the neutral slot uniquely. The pairwise linking number $\mathrm{Lk}$ and the Milnor triple linking $\bar\mu(123)$ do not qualify. The even-twist carrier is a two-component link, so $\bar\mu(123) \equiv 0$ on every carrier. $\mathrm{Lk}(T(2,2k)) = k \neq 0$ on every carrier. Neither is nonzero on exactly one vector slot.

**The group-structure data does force the label.**

Topology cannot force the label, but the $\mathrm{SU}(2)_L 	imes \mathrm{U}(1)_Y$ group assignment can. The genuine missing input is the alignment of the two vector slots with the $\mathfrak{su}(2)_L$ Cartan–Weyl basis. Given the `EWGroupAssignment`, the label is derived: the neutral slot is the Cartan slot, the charged slot is the complementary root slot. The group datum itself remains the open conjectural input.
<!-- FILE_END: electroweak-triplet-charge-spin-from-involution.md -->

<!-- FILE_START: ew-slot-far-commutation-obstruction.md -->
*Let $A$ be a ring. Let $\sigma_1, \sigma_3, \sigma_5 \in A$ be the braid generators hosting the electroweak carriers on the disjoint strand-pairs. These are subject to the braid far-commutation relation $\sigma_i \sigma_j = \sigma_j \sigma_i$ for $|i - j| \ge 2$. Let $\mathcal{A}_{\mathrm{slot}} \subseteq A$ be the subalgebra they generate. Suppose $J_1, J_2, J_3 \in A$ realise an $\mathfrak{su}(2)_L$ adjoint structure relation $\lbrack J_1, J_2 \rbrack = J_3$ with $J_3 \ne 0$. Then $J_1$ and $J_2$ cannot both lie in $\mathcal{A}_{\mathrm{slot}}$. The non-abelian $\mathrm{SU}(2)_L$ structure therefore cannot be realised purely among the far-commuting slots.*

### Statement (formal)

The slot indices $1, 3, 5$ are pairwise far apart. Thus $\sigma_1, \sigma_3, \sigma_5$ pairwise commute. Consequently, the subalgebra $\mathcal{A}_{\mathrm{slot}} = \langle \sigma_1, \sigma_3, \sigma_5 \rangle$ is commutative. Every commutator $\lbrack x, y \rbrack = xy - yx$ vanishes for $x, y \in \mathcal{A}_{\mathrm{slot}}$. The three carriers $W \leftrightarrow \sigma_1^{4}$, $Z \leftrightarrow \sigma_3^{6}$, $H \leftrightarrow \sigma_5^{8}$ pairwise commute.

The obstruction is the incompatibility of two facts:

1. **Commuting operators have vanishing bracket.** For $x, y \in \mathcal{A}_{\mathrm{slot}}$, $\lbrack x, y \rbrack = 0$.
2. **The $\mathfrak{su}(2)_L$ adjoint is non-abelian.** Its generators satisfy $\lbrack J_a, J_b \rbrack = \varepsilon_{abc} J_c \ne 0$. A nonzero bracket forbids commutation.

If both $J_1, J_2 \in \mathcal{A}_{\mathrm{slot}}$, then $\lbrack J_1, J_2 \rbrack = 0$ by (1), contradicting $J_3 \ne 0$ by (2). At least one $\mathfrak{su}(2)_L$ generator must escape the slot subalgebra.

### What this forces

This result is a structural exclusion. It proves an impossibility, not a numerical near-miss. It establishes where the missing structure must reside.

The far-commutation relation covers only pairs with $|i - j| \ge 2$. The adjacent generators $\sigma_2, \sigma_4$ bridge strand-pairs $2	ext{--}3$ and $4	ext{--}5$. These do not commute with the slots. The categorical linking operation $\mathrm{Lk}_R^{(k)}$ braids between strand-pairs through precisely these generators. The non-abelian $\mathrm{SU}(2)_L$ structure must therefore be carried by the inter-slot linking, not by the individual slots.

This narrows the group-assignment postulate. The residual $\mathrm{SU}(2)_L 	imes \mathrm{U}(1)_Y$ input is a property of the bracket-carrying linking data, not of the mutually commuting slots. The label lives where the non-abelianness lives: in the linking, not the slots.

### Lean structure

The formalisation is purely algebraic over a generic ring:

- `bracket_eq_zero_of_commute`: commuting elements have zero commutator.
- `nonabelian_bracket_forbids_commute`: the crux.
- `commute_of_mem_closure`: the submonoid generated by a pairwise-commuting set is commutative.
- `slotSubmonoid_commutative`, `carriers_commute`: the slot subalgebra is mutually abelian.
- `su2L_nonabelianness_not_in_slots`, `su2L_generator_escapes_slots`: the capstone obstruction and its positive form.

All are verified sorry-free.
<!-- FILE_END: ew-slot-far-commutation-obstruction.md -->

