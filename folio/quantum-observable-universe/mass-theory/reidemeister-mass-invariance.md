**Conjecture (conditional on [Quarks as Borromean-linked unknots in the exceptional divisor](#conj:borromean-quark)).**
The topological mass formula is a knot invariant (R-I, R-II,
R-III).  The binding energy of linked particles is an
embedding invariant (R-II, R-III but not R-I).  Shell
transitions are R-I moves on the embedding. *(The three
Reidemeister invariances follow from the hyperbolic-volume
invariant and the embedding structure; the shell-transition
R-I reading is the conjectural part.)*

**The three Reidemeister moves.**

Every deformation of a knot diagram decomposes into a sequence
of three local moves:

- **R-I** (curl): add or remove a single crossing (writhe
  changes by $\pm 1$).
- **R-II** (poke): add or remove a pair of crossings with
  opposite signs (writhe unchanged).
- **R-III** (slide): move a strand past a crossing (crossing
  number unchanged).

**Topological mass: invariant under all three.**

The bare mass of a particle is determined by the hyperbolic
volume of its knot complement and the per-block density:

$$
  m_{\mathrm{bare}}(K) = 
  m_e \cdot \frac{\mathrm{Vol}(S^3 \setminus K) \, \rho(K)}{\hbar_q^2}.
$$

The hyperbolic volume is a **topological invariant** of the
knot type — it does not depend on the diagram — and the
per-block density $\rho(K)$ is computed from the Markov trace
of the braid closure, itself a knot invariant.  Since
Reidemeister's theorem states that two diagrams represent the
same knot if and only if they are related by a finite sequence
of R-I, R-II, R-III moves:

$$
  m_{\mathrm{bare}}
   \text{is invariant under R-I, R-II, R-III.}
$$

The electron mass $\mathfrak{m}_e \approx 0.511$ MeV (from vacuum drag, since
$\mathrm{Vol}(T_{2,3}) = 0$) does not change when the electron
is excited.  The proton mass $\mathfrak{m}_{\mathfrak{p}} \approx 938$ MeV
(from $\mathrm{Vol}(\mathcal{B}_3)$) does not change when the
atom is ionised.  Mass is a property of the **knot type**, not
the diagram.

**Binding energy: invariant under R-II and R-III only.**

The binding energy of a linked pair (electron--proton, or
nucleon--nucleon) is the crossing energy of the Hopf link
connecting them:

$$
  \mathfrak{E}_{\mathrm{bind}}
  = 
  \sum_{\text{crossings of link}}
  \epsilon_i \cdot q^{\pm 1}
$$

where the sum runs over the crossings of the **embedding** of
one particle's knot inside the other's Seifert surface.

- **R-III** (strand slide): rearranges crossings without
  changing their number or signs.  The crossing energy sum
  is invariant. $\checkmark$

- **R-II** (poke): adds two crossings of opposite sign.  Their
  contributions to the crossing energy are $+q \cdot \epsilon$
  and $-q^{-1} \cdot \epsilon$.  In the Skein resolution, the
  pair resolves to $(q - q^{-1}) \cdot \epsilon \cdot L_0$,
  where $L_0$ is the smoothed state.  For a virtual pair
  (the two crossings are adjacent), $L_0$ is the original
  link and the contributions cancel to leading order.  The
  binding energy is invariant. $\checkmark$

- **R-I** (curl): adds a single crossing.  This changes the
  writhe by $\pm 1$ and adds a crossing energy contribution
  $\pm q^{\pm 1} \cdot \epsilon$ that does **not** cancel.
  The binding energy **changes**. $\times$

$$
  \mathfrak{E}_{\mathrm{bind}}
   \text{is invariant under R-II, R-III but \textbf{not} R-I.}
$$

**Shell transitions are R-I moves.**

When a photon is absorbed by the hydrogen atom, the electron
trefoil $T_{2,3}$ undergoes a **Reidemeister I move** within its
Hopf link to the proton: a curl is added to the trefoil diagram
at the exceptional divisor.  The writhe changes from $w$ to
$w + 2$ (a pair of R-I moves adding two curls to preserve the
knot type's minimal crossing structure):

$$
  n \to n + 1
  \qquad\Longleftrightarrow\qquad
  w \to w + 2
  \qquad\Longleftrightarrow\qquad
  \text{two R-I moves on the embedding.}
$$

The bare mass $\mathfrak{m}_e$ is unchanged (R-I is a knot invariant).
The binding energy $E_n = -13.6/n^2$ eV changes (R-I is NOT
an embedding invariant).  The difference $\Delta E = E_{n+1} - E_n$ is the photon energy.

**Summary.**

| Quantity | R-I | R-II | R-III | Physical meaning |
|----------|:---:|:----:|:-----:|-----------------|
| Bare mass | $\checkmark$ | $\checkmark$ | $\checkmark$ | Particle identity (knot type) |
| Binding energy | $\times$ | $\checkmark$ | $\checkmark$ | Bound state energy (embedding) |
| Shell number $n$ | $\times$ | $\checkmark$ | $\checkmark$ | Writhe level of embedding |
| Knot type | $\checkmark$ | $\checkmark$ | $\checkmark$ | Which particle it is |
| Writhe $w$ | $\times$ | $\checkmark$ | $\times^*$ | Diagram-dependent |

${}^*$R-III preserves writhe but is not the only invariance
of writhe; writhe is a regular isotopy invariant (R-II +
R-III), not a knot invariant (R-I + R-II + R-III).

**Physical consequence.**

A particle's **identity** (which knot type: electron, muon,
proton, neutron) is determined by R-I + R-II + R-III invariants
— the topological knot type.  A particle's **state** (which
shell, which orbital) is determined by R-II + R-III invariants
— the regular isotopy class of the embedding.  The difference
between identity and state is precisely one Reidemeister move:
R-I.

This is why an excited hydrogen atom is still hydrogen: the
electron is still a trefoil (knot type unchanged by R-I).  But
it is in a different state: the trefoil's writhe is different
(embedding changed by R-I), and the binding energy differs.

**Archimedean specialisation.** What follows sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
