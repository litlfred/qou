Proof strategy for
[archimedean QOU is the standard-part of surreal QOU](#conj:archimedean-stpart).
This remark records *how* one would attempt the proof, not the proof
itself; the conjecture remains open.

The conjecture is the *category-level* counterpart of
[classical-limit-stpart](#conj:classical-limit-stpart). Reduce
to that conjecture via:

1. **Functorial reduction.** Show
   $\mathrm{St}_{\mathrm{QOU}} = (\mathrm{St}, \mathrm{St}, \mathrm{St},
   \mathrm{St})$ — the standard-part applied to each component of the
   QOU tuple $(\mathbf{C}, \varTheta, G, \mathcal{S})$.

2. **Reduce each component**:
   - $\mathbf{C} = \mathrm{Rep}_{\mathbf{No}}(\mathrm{SU}_q(2))$ at
     $q = 1 + \varepsilon$: $\mathrm{St}$ recovers
     $\mathrm{Rep}_{\mathbb{R}}(\mathrm{SU}(2))$ by
     [classical-limit-stpart](#conj:classical-limit-stpart).
   - $\varTheta : \mathbf{1} \to A$: just an element of a hom-space;
     $\mathrm{St}$ acts entry-wise.
   - $G = \mathrm{Aut}(A)$: a functorial gauge group; standard-part
     of an algebraic group object. This is the categorical
     counterpart of the archimedean realization $\tau$ of
     [fibre functor rigidity](#rem:fibre-functor-rigidity) — the
     image of the rigid monoidal embedding into $\mathbb{R}$-linear
     endomorphisms.
   - $\mathcal{S}$: state bundle; standard-part of fibre.

3. **Verify axioms.** Each $\varepsilon$-relaxed axiom (Frobenius,
   observability, volume, vacuum) becomes the strict axiom under
   $\mathrm{St}$ — content of conjectures
   [infinitesimal-frobenius](#conj:infinitesimal-frobenius),
   [infinitesimal-observability](#conj:infinitesimal-observability),
   [vacuum-epsilon](#conj:vacuum-epsilon).

4. **Essential surjectivity.** Every archimedean QOU lifts (set
   $\varepsilon = 0$ trivially). This direction is automatic.

**Required infrastructure**:

- The five sub-conjectures above (or worked examples).
- A `Functor` instance from `QOU_𝐍𝐨^ε` to `QOU_ℝ` in Lean.
- `CategoryTheory.MonoidalFunctor` interaction with $\mathrm{St}$.

**Falsification path.** Exhibit an $\varepsilon$-relaxed surreal
QOU whose standard-part image violates a strict QOU axiom (e.g.
the Frobenius pairing of the standard-part has positive nullity).
This would require an infinitesimal that becomes non-infinitesimal
under standard-part — impossible by the definition of $\mathrm{st}$.

**Provability assessment.** Structurally clean once the
sub-conjectures are settled. Mainly bookkeeping over the four
QOU components.
