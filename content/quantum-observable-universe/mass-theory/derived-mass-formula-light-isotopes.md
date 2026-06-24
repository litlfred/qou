**Proposition.**
*The strict derived mass formula*

$$
\begin{aligned}
\mathcal{M}(Z, N) &= Z \mathfrak{m}_{\mathfrak{p}} + N \mathfrak{m}_{\mathfrak{n}} + Z m_e \\
                  &\quad + \alpha \bigl(\Phi_1 - 2[3]_q \Phi_2 + H_A^2 \Phi_3\bigr) \\
                  &\quad + \Delta_{W}(Z, N) + \Delta_{T=1}(Z, N)
\end{aligned}
$$

*with each term derived (no fitting):*

- *$\alpha = m_e \cdot 8G$ (Borromean prefactor;
 [binding scale](#prop:binding-scale-catalan));*
- *$\Phi_1, \Phi_2, \Phi_3$ extracted from per-generator transfer-matrix
 chains using only the inter-nucleon generators (positions $3k+2$ for
 $k = 0, \ldots, A{-}2$);*
- *$\Delta_W = -m_e \cdot H_q((2,2)) \cdot \min(Z, N)/A$
 (Wigner $T=0$ pn pairing,
 [Wigner np pairing](#prop:wigner-np-pairing));*
- *$\Delta_{T=1} = -m_e \cdot H_q((2,2)) \cdot (n_{pp} + n_{nn})/A$
 (natural $T=1$ isovector extension using the same self-conjugate
 partition $(2,2) \vdash 4$ and the same $1/A$ normalisation, with
 $n_{pp} = Z(Z{-}1)/2$ and $n_{nn} = N(N{-}1)/2$);*

*reproduces the atomic masses of all isotopes from $\mathfrak{p}$
through $^7$Li to sub-percent accuracy.*

**Empirical scorecard at $q_0 = 1.109978595554181\ldots$ (50 dps):**

See [Table 1](#tbl:derived-mass-formula-light-isotopes-table1-data).

**Proton-neutron mass splitting:**
$\Delta\mathfrak{m}_{\mathfrak{n}-\mathfrak{p}} = 1.293332$ MeV
matches CODATA exactly (preserved by inter-gen direct convention,
since free nucleons have $\Phi = 0$).

**Binding under-prediction.**
*The same formula systematically under-predicts nuclear binding
energies by $30\%$ to $76\%$ across light isotopes:*

See [Table 2](#tbl:derived-mass-formula-light-isotopes-table2-data).

*The under-binding pattern is structural: the formula misses an
intra-shell binding mechanism present in nature. Closing the gap
universally requires a new derived term (not phenomenological
patches), which remains an open research direction.*

**Witness:** `derived-only-formula.witness.json`.

**Scope.** The formula is derived from Hecke partition theory and the
paper's atomic-mass framework; no continuous parameters are fitted, and
no choices were made by selecting from a menu of variants. The atomic
mass agreement to sub-percent across $A = 1$ to $7$ — including the
unfitted extension to $^6$Li and $^7$Li — is **predictive**, not
calibrated.

The systematic binding under-prediction is the formula's principal
limitation. Closed-form patches that improve specific isotopes (D, T,
$^3$He, $^4$He) to within 7% can be constructed from $H_q((2,1))$ and
$[3]_q^2$ candidates (see witnesses
`he3_tighten_pp.py`, `d_tighten_k3.py`, `he4_tighten_doubly_magic.py`),
but each such patch involves a discrete choice between several
algebraically-natural variants — hence is technically fitted (model
selection).

**Structural extension to $A \geq 5$.**
The shell-correction conjecture
(Term 7 shell correction)
identifies the binding gap at $A \geq 5$ with the GB-filtration
level $\ell = 5$ (height-6 partitions) of the brane-tower
spectral sequence. Adding the conjectural Term 7 to the formula
above is expected to bridge the binding gap structurally; the
specific shadow-price form is open research.
