**Conjecture (symmetric-crystal pair production).**
*Let $H_n(R, q)$ be the Iwahori–Hecke algebra of type $A_{n-1}$
with [Hecke normal forms](#def:hecke-normal-form) $\{T_w\}$, and let
$\mathrm{Cryst}(\mathfrak{sl}_n)$ be its associated Kashiwara crystal
under [crystal-graph realisation](#conj:crystal-graph-realization).
Fold the $\mathfrak{sl}_n$ Cartan datum into a Type B Cartan datum
along the Dynkin involution $i \mapsto \bar i = n - i$, equivalently
the $\mathbb{Z}/2\mathbb{Z}$ bar-involution
$T_w \mapsto \overline{T_w}$ that sends $q \mapsto q^{-1}$ and reverses
crossings.  The resulting symmetric crystal
$\mathrm{Cryst}^{\mathrm{sym}}(\mathfrak{so}_{2n+1})$ admits no
Kashiwara lowering operator $\tilde f_i$ as a unimodal step from a
bar-invariant source; every step is a paired operator
$(\tilde f_i, \tilde f_{\bar i})$.  Consequently, a transition*

$$
  v_0 \;\xrightarrow{\;(\tilde f_i, \tilde f_{\bar i})\;}\; v_-\,\sqcup\,v_+,
$$

*from a bar-invariant highest-weight vector $v_0$ produces two
descendants $v_-, v_+$ whose Hecke normal forms are bar-conjugates,
$\overline{T_{v_-}} = T_{v_+}$.  Identifying $v_-$ with a chiral
particle and $v_+$ with its CPT antiparticle, the symmetric crystal
forbids the production of a single chiral excitation from a non-chiral
source: any descendant set is a disjoint union of bar-conjugate
pairs.*

**Algorithmic role (charge-conservation kill switch).**
*The Gröbner–Shirshov reduction engine therefore enforces matter–
antimatter pairing structurally: at each crystal step it applies the
folded operator pair atomically, so an internally generated
intermediate that would carry a single net chirality is unreachable.
The Hecke normal forms produced by the engine are bar-invariant by
construction (i.e. fixed under $T_w \mapsto \overline{T_w}$), and any
candidate normal form failing this test is rejected before further
expansion.  This converts CPT and charge conservation from
combinatorial post-conditions into intrinsic invariants of the
crystal traversal — no custom $\mathbb{Z}/2\mathbb{Z}$ rules required
in the engine code.*

**Why a conjecture and not a theorem.**
*The Type B folding of $\mathfrak{sl}_n$ Kashiwara crystals into
$\mathfrak{so}_{2n+1}$ symmetric crystals is established at the level
of generic quantum-group representations
\cite{kashiwara1991, lecouvey2007}, and the bar-involution is intrinsic
to the KLR canonical basis \cite{khovanovlauda2009, brundankleshchev2009}.
What remains conjectural in this manuscript is that the folded
operators on the cyclotomic quotient realising $H_n(R, q)$ realise
exactly the matter/antimatter pairing of the topological ansatz: that
the bar-conjugate pair on a single Type B crystal node corresponds to
a CPT pair of QOU particles.  The empirical evidence is the
$\det \rho_\lambda(w) \cdot \det \rho_{\lambda'}(w) = \pm 1$
identity for every conjugate-partition pair $(\lambda, \lambda')$
([conjugate-pair det law](computations/det_pair_law.py));
this identity is the bar-involution acting on Wedderburn blocks and
is the strongest available shadow of the conjecture without a full
KLR-folding proof.*
