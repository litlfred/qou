The many-body binding weight of the jet-order filtration factorises as
$w_n(K) = M_n(A)\,\mathrm{Vol}_n(K)$, where $\mathrm{Vol}_n(K)$ is the hyperbolic
volume of the $n$-body sub-link of the building-block link $\mathcal{B}_K$ and
$M_n(A)$ is a body-order multiplicity. The volume factor is the isospin ($T_3$)
carrier — the ${}^3\mathrm{H}$/${}^3\mathrm{He}$ mirror split is supplied by
$\mathrm{Vol}({}^3\mathrm{H}) > \mathrm{Vol}({}^3\mathrm{He})$ with no fit — while the
multiplicity $M_n(A)$ was left open. The crossing/coordination structure of
$\mathcal{B}_K$ supplies a topological reading of $M_n(A)$.

## The multiplicity read off the crossing/coordination structure

Write the **per-nucleon coordination number** $z(A) = A-1$ (the number of nucleon–nucleon
bonds incident to one nucleon in the fully coordinated cluster) and the **total bond
count** $C(A,2) = \tfrac{1}{2}A(A-1)$. Reading the required multiplicity straight off the
AME2020 binding energies, $M_{\mathrm{need}}(A) = B_{\mathrm{AME}} / (m_e\,\mathrm{Vol}_A)$:

| isotope | $\mathcal{B}_K$ | $M_{\mathrm{need}}$ | $z = A-1$ |
| --- | --- | ---: | ---: |
| ${}^3\mathrm{H}$ | $8_{11}$ | $2.003$ | $2$ |
| ${}^3\mathrm{He}$ | $\mathrm{L6a4}$ (Borromean) | $2.061$ | $2$ |
| ${}^4\mathrm{He}$ | $\mathrm{L6a4}$ base | $7.557$ | $3$ |

For the **non-magic $A=3$ pair the multiplicity is the per-nucleon coordination number**
$z = A-1 = 2$, matched to better than $3\%$ with no free parameter. The doubly-magic
${}^4\mathrm{He}$ carries an additional closed-shell enhancement
$M_{\mathrm{need}}/z \approx 2.52 \approx a_D^{(4)}$, the super-exponential
Schur–Weyl period; this factor over-shoots the $A=3$ pair by $\approx 30\%$, so it is a
magic-shell enhancement rather than a universal factor.

The deuteron sits on the Seifert-fibred Hopf link, where $\mathrm{Vol} = 0$ and any
volume product vanishes. The **crossing structure survives** there — the Hopf link has
crossing number $2$, linking number $|\mathrm{lk}| = 1$, and per-nucleon coordination
$z = 1$ — so the coordination carrier is the natural non-vanishing replacement for the
volume on the two-body sub-link.

That the carrier is a *coordination count* and not a Gauss linking number is now proved rather
than posited ([the Brunnian binding channel](#prop:brunnian-binding-channel)). The ${}^3\mathrm{He}$
and ${}^4\mathrm{He}$ carriers are Borromean, hence Brunnian: every pairwise linking number
vanishes, so a linking-number multiplier would read zero for exactly these nuclei. In the proved
crossing-energy channel split the signed (linking-number) channel is empty for a Brunnian pair and
the binding is carried by the sign-blind coordination-count channel, which is bar-odd and therefore
complementary to the bar-even mass self-weight $\mathrm{lw}$. The deuteron Hopf case
($\mathrm{lk} = z = 1$) is the boundary where the two invariants coincide; they diverge at
$A \geq 3$, where only the coordination count is non-vanishing.

## Extension: $\alpha$-cluster coordination for $A > 4$

The heavier magic nuclei ${}^{16}\mathrm{O}$ and ${}^{40}\mathrm{Ca}$ are not single
hyperbolic links but $\alpha$-conjugate clusters. The coordination principle lifts one
level: treating each ${}^4\mathrm{He}$ as one node and counting $\alpha$–$\alpha$
coordination bonds,

$$
  B(n_\alpha) \approx n_\alpha\,B({}^4\mathrm{He}) + N_{\mathrm{bonds}}\,b_{\alpha\alpha}.
$$

For a **simplex** cluster ($n_\alpha \le 4$, complete $\alpha$-graph realisable up to the
tetrahedron) $N_{\mathrm{bonds}} = C(n_\alpha, 2)$, and the residual per bond is a
near-constant $b_{\alpha\alpha} \approx 2.41\,\text{MeV}$ (${}^{12}\mathrm{C}$: $2.425$;
${}^{16}\mathrm{O}$: $2.406$). These per-bond $b_{\alpha\alpha}$ values are empirical near-constants read off the AME data (not derived — the same data-selected $\alpha$-$\alpha$ coefficient honestly labelled in [`rem:alpha-cluster-model-g-closure`](#rem:alpha-cluster-model-g-closure)), and the $M_{\mathrm{need}}/z \approx 2.52$ closed-shell factor is likewise an AME read rather than a derived Schur-Weyl period. The single $\alpha$–$\alpha$ pair ${}^8\mathrm{Be}$ gives
$\approx 0$, consistent with its being unbound relative to two $\alpha$-particles. For
$n_\alpha \ge 5$ the complete graph over-counts — not all pairs can be nearest neighbours
in three dimensions — and the per-bond residual falls, so the coordination number
saturates to a geometric close-packing count. This reproduces the classical
Hafstad–Teller $\alpha$-bond picture with $N_{\mathrm{bonds}}$ read as the
$\alpha$-cluster coordination number, the same principle as $z = A-1$ one level up.
