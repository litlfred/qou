The unified knot mass formula
([unified knot mass](#thm:knot-mass-formula-unified)) sums six
structural terms. Empirically, however, **different term subsets
dominate in different $A$ regimes**, and naïve additive summation
produces double-counting. This proposition documents the
regime-switching structure and resolves the apparent failure of
paper's BW+chirality formula at $A = 2$.

**Proposition.**
*Let $B(Z, N)$ denote the binding energy of an isotope with $A = Z + N$.
The following regime-switched formula matches AME to $\leq 5\%$ for
$A \leq 4$:*

$$
  B(Z, N)
  \;=\;
  \begin{cases}
    B_{\mathrm{SW}}(Z, N) + m_e\,\tau(C_{\dim_q}^{H_3})
      & \text{if } A = 2, \\[4pt]
    B_{\mathrm{BW}+\chi}(Z, N)
      & \text{if } 3 \leq A \leq 4, \\[4pt]
    B_{\mathrm{BW}}(Z, N) + B_{\mathrm{shell}}(A)
      & \text{if } A \geq 5,
  \end{cases}
$$

*where:*

- *$B_{\mathrm{SW}}(Z, N) = E_0 \cdot \bigl(|\mathrm{tr}_M(\mathrm{free})| - |\mathrm{tr}_M(\mathrm{atom})|\bigr)$ is the Schur–Weyl descended
 binding ([Schur–Weyl decomposition](#prop:schur-weyl-mass-decomposition)).*
- *$m_e \cdot \tau(C_{\dim_q}^{H_3}) = m_e(2 + 1/[2]_q) \approx 1.276\;\mathrm{MeV}$ is the universal
 Frobenius co-Casimir correction
 ([partition-sum residual](#prop:partition-sum-proton-residual)).*
- *$B_{\mathrm{BW}+\chi}$ is the paper's BW + chirality formula
 ([figure-eight BW coefficients](#thm:six-term-mass-formula-complete))
 with chirality factor $1 - h^2$ for $A = 3$ and $(1 - h^2)^2$ for $A = 4$.*
- *$B_{\mathrm{BW}}$ is the standard BW formula without chirality, plus a shell correction for magic numbers.*

**Unification: paper's BW coefficients are Hecke-derived $q$-integer products.**

*Per
[$q$-integer mass formula](#conj:q-integer-mass-formula),
each BW coefficient has an exact $q$-integer expression derived
from the Hecke algebra $H_3(R, q)$:*

See [Table 1](#tbl:mass-formula-regime-switching-table1-data).

*The exact relation $a_{\mathrm{asym}} = \frac{3}{2} \lambda_V$ is
**forced** by the $q$-integer form (both involve $[2]_q[7]_q$,
prefactors $3$ vs $2$) — an exact algebraic identity that is only
approximate in empirical BW fits. Similarly
$\lambda_S / \lambda_V = [4]_q^2 / ([2]_q [7]_q)$ is exact,
reflecting the $\sigma_1$ vs $\sigma_0$ crossing ratio.*

*So the unification **is** already in the paper: BW is Hecke-trace
data, specifically products of $q$-integers counting crossings in
the $B_3$ / $4_1$ knot topologies.*

**Why regimes switch: topology, not just $A$.**

*The BW coefficients contain $q$-integers that count crossings in
a **specific topology**: $[7]_q$, $[4]_q$ are proton's internal
crossing counts; $[6]_q$ is the Borromean link $B_3$'s crossings.
These values are structurally tied to the $A \geq 3$ Borromean /
figure-eight topology.*

*For $A = 2$ (deuteron), the topology is a **satellite knot**, not
Borromean: the deuteron braid is $\varrho_{\mathfrak{p}} \cdot
\varrho_{\mathfrak{n}} \cdot \sigma_{\mathrm{pn}}$ — two nucleon
trefoils tied by one inter-nucleon crossing. The Borromean-specific
crossing counts $[6]_q, [7]_q, [4]_q$ **do not apply** to this
topology; the dominant dynamics are in the single inter-nucleon
crossing $\sigma_{\mathrm{pn}}$ and the two internal nucleon
Markov traces.*

*This is why paper's BW formula fails for $D$: it substitutes the
Borromean-topology $q$-integer coefficients into an $A$-dependent
framework ($\lambda_V \cdot A$, $\lambda_S \cdot A^{2/3}$, etc.),
but those coefficients were derived for the Borromean topology,
not the satellite topology of $D$. The regime switch is
**topological**, and $A = 2$ vs $A \geq 3$ is the topological
transition point (single pair vs Borromean triple).*

**Why $A = 2$ breakdown of BW.**

*At $A = 2$ the standard BW formula gives*

$$
  B_{\mathrm{bulk}}^{(A=2)}
  \;=\; 2 \lambda_V - 2^{2/3} \lambda_S - \delta_P/\sqrt{2}
  \;\approx\; 31.3 - 27.4 - 8.4 \;=\; -4.5\;\mathrm{MeV},
$$

*negative. The BW volume term does not exceed surface + pairing
at $A = 2$: the liquid-drop approximation has no droplet to speak
of with only two nucleons. Multiplying by any chirality factor
$a_K > 0$ keeps $B_{\mathrm{pred}} < 0$, which is unphysical. The
$D$ chirality probe `d_chirality_probe.py` verified this: no
choice of $a_K \in [-2, 2]$ with the form
$B = a_K \cdot B_{\mathrm{bulk}}$ matches $B_{\mathrm{AME}}$
positively; the closest positive match requires $a_K < 0$
(negative, not a chirality factor).*

**Why SW+Frob works at $A = 2$.**

*At $A = 2$ the atomic braid has only $1$ inter-nucleon crossing
on top of the intra-nucleon Hecke words. The Markov trace
$|\mathrm{tr}_M(T_w)|$ captures nearly all of the binding, and
the universal Frobenius correction
$m_e(2 + 1/[2]_q) \approx 1.28\;\mathrm{MeV}$ accounts for the
remaining per-vortex substrate cost. Result: $B_D^{\mathrm{pred}}
\approx 2.27\;\mathrm{MeV}$ vs $B_{\mathrm{AME}} = 2.22\;\mathrm{MeV}$
($+2.1\%$).*

*The Schur–Weyl pipeline describes $A = 2$ because:*

1. *Only $p(6) = 11$ partitions to sum over.*
2. *Max Specht dimension $f^\lambda = 16$ — tractable numerically.*
3. *No collective motion is present (no liquid-drop approximation needed).*
4. *Only one inter-nucleon crossing — the tower structure is minimal.*

**Why BW+$\chi$ works at $A \geq 3$.**

*Starting at $A = 3$, the atomic braid has enough crossings that
**collective** partition channels dominate — the full Markov
trace is small (exponentially suppressed as $\sim 0.5^A$) but
the Wedderburn-weighted character sum
$\sum_\lambda w_\lambda \chi_\lambda$
remains large through specific collective partitions
$\lambda \vdash 3A$. Paper's BW formula captures this collective
content via the Hecke-algebra-derived coefficients
$\lambda_V = 2[2]_q[7]_q m_e$, $\lambda_S = 2[4]_q^2 m_e$, etc.
The chirality factor $1 - h^2$ is the $H_3$-level figure-eight
topology correction ([figure-eight BW coefficients](#thm:six-term-mass-formula-complete)).*

**No double-counting: SW and BW are not independent.**

*The paper's $B_{\mathrm{bulk}}$ coefficients are derived from
the Wedderburn channel weights $(w_{\mathrm{sym}}, w_{\mathrm{std}}, w_{\mathrm{alt}})$
times character differences $\chi_{4_1}(\lambda) - \chi_{B_3}(\lambda)$
([figure-eight BW coefficients](#thm:six-term-mass-formula-complete) proof).
The Schur–Weyl descended trace $|\mathrm{tr}_M(T_w)|$ is
$\sum_\lambda w_\lambda \chi_\lambda(T_w)$ for the **specific**
braid word $T_w$, weighted by $w_\lambda$. The two are computing
the same underlying partition sum — paper's BW is the $A \geq 3$
collective limit where specific character combinations dominate,
while SW is the exact evaluation that works best when individual
partition contributions are traceable. **Summing both double-counts.**
The regime-switching formula avoids this by choosing the dominant
computation per $A$.*

**Paper D chirality assignment is a category error.**

*The paper assigns $D \to (1 + h)$ as chirality factor; empirically
this fails by $-353\%$. Probe `d_chirality_probe.py` tested $13$
alternatives and continuous optimisation in $a_K \in [-2, 2]$;
no positive chirality factor fits. The resolution: **$D$ is not
in the BW regime at all**, so asking for its chirality factor is
a category error.*

*The paper's figure-eight BW derivation
([figure-eight BW coefficients](#thm:six-term-mass-formula-complete))
explicitly starts from the $4_1$ knot on $H_3(R, q)$ and derives
$a_K = 1 - h^2$ from the character $\chi_{4_1}(2,1) = 2 - [3]_q
= -1 - h^2$. For $D$ (satellite topology, $H_6(R, q)$), that
derivation does not apply; the satellite-knot character sum is a
different object.*

*The correct $D$ prediction is via Schur–Weyl on $H_6(R, q)$ directly
(our pipeline): $B_D^{\mathrm{pred}} = 2.27$ MeV vs $B_{\mathrm{AME}}
= 2.22$ MeV ($+2.1\%$). The "chirality factor" for $D$ under this
pipeline is implicitly captured by the braid word $T_w$ itself,
which already distinguishes positive and negative crossings
through the Hecke eigenvalues $(q, -q^{-1})$.*

*Recommended update to
[figure-eight BW coefficients](#thm:six-term-mass-formula-complete):*

*Add a scope note: "The $a_K$ chirality factor applies to
isotopes in the Borromean / $4_1$ topology ($A \geq 3$). For
$A = 2$ (satellite-knot topology), the formula does not apply."*

**Unification via dominant-term selection.**

*The deep statement is that the 6-term unified formula is a sum
over **complementary** contributions, each dominant in a different
regime. A single additive formula cannot work because different
regimes use different structural content from the same algebraic
objects. This is the mathematical reality: no single closed form
covers all $A$ — the regime switch is fundamental.*

*A future unification target is a **self-selecting** formula that
interpolates between SW+Frob ($A \leq 2$) and BW+$\chi$ ($A \geq 3$)
— for example via a smooth weighting $w_A \in [0, 1]$ that
transitions at $A = 2.5$. At present this is empirical; the
categorical derivation of $w_A$ is open.*

**Integrated witness table (from `mass_formula_6term.py`).**

See [Table 2](#tbl:mass-formula-regime-switching-table2-data).

*All predictions use **zero** fitted constants beyond $q_0$ and
$m_e$ (equivalently $E_0 = 0.782\;\mathrm{MeV}$).*
