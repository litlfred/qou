Every neutral atom is a composite knot configuration built from protons, neutrons, and electrons via the three generation operations ([knot-particle generation](#def:knot-particle-generation)). For an isotope with atomic number $Z$, neutron number $N$, and mass number $A = Z + N$, the composite knot formula decomposes into $k_\alpha = \min(\lfloor Z/2 \rfloor, \lfloor N/2 \rfloor)$ closed tetrahedral $\alpha$-clusters plus excess valence nucleons and $Z$ electronic trefoils.

$$
  Z\mathfrak{p} \oplus N\mathfrak{n} \oplus Z \cdot T_{2,3}
  \;=\;
  k_\alpha \alpha \oplus (Z - 2k_\alpha)\mathfrak{p} \oplus (N - 2k_\alpha)\mathfrak{n} \oplus Z \cdot T_{2,3}.
$$

Here $\mathfrak{p} = \mathcal{B}_3(\mathfrak{u}\mathfrak{u}\mathfrak{d})$ and $\mathfrak{n} = \mathcal{B}_3(\mathfrak{u}\mathfrak{d}\mathfrak{d})$ are three-strand flavored Borromean baryons ([Borromean baryon](#def:borromean-baryon)), $\alpha = 2\mathfrak{p} \oplus 2\mathfrak{n}$ is the closed four-nucleon $K_4$ singlet, $T_{2,3} = 3_1$ is the electron trefoil ([fermions are knots, bosons are links](#prop:fermion-boson-knot-link)), and $\oplus$ denotes Hopf linking. Every constituent has Seifert genus at most $4$ ([embeddability closure](#thm:embeddability-closure)) and is generated from the torus basis via skein crossing changes ([generation completeness](#thm:generation-completeness)).

**Parameter-free nuclear binding and neutral atomic mass.**

On the three-dimensional close-packed nuclear shell ball of $A$ nucleons with simplicial face counts $\bigl(f_1^{\mathrm{shell}}(A), f_2^{\mathrm{shell}}(A), f_3^{\mathrm{shell}}(A)\bigr)$, the nuclear binding energy $B_{\mathrm{QOU}}(Z, N)$ and neutral atomic mass $M_{\mathrm{QOU}}(Z, N)$ are determined without free parameters by the aether parameter $q_0$ ($q_{2\mathrm{t}} = 1.10997860\ldots$) and electron mass scale $m_e = 0.51099895\;\mathrm{MeV}$.

$$
  B_{\mathrm{QOU}}(Z, N)
  \;=\;
  f_1^{\mathrm{shell}}(A)\,b_2
  + f_2^{\mathrm{shell}}(A)\,w_3
  + f_3^{\mathrm{shell}}(A)\,w_4^{(H_4)}
  - E_{\mathrm{HO}}^{\mathrm{sym}}(A)
  - E_{\mathrm{sym}}^{\mathrm{F}}(Z, N)
  - E_{\mathrm{SO}}(Z, N)
  + \Delta_{\mathrm{TL}}(Z, N)
  - E_{\mathrm{C}}^{\mathrm{FCC}}(Z, A),
$$

$$
  M_{\mathrm{QOU}}(Z, N)
  \;=\;
  Z\,m_{\mathfrak{p}}(q_{2\mathrm{t}})
  + N\,m_{\mathfrak{n}}(q_{2\mathrm{t}})
  + Z\,m_e
  - B_{\mathrm{QOU}}(Z, N).
$$

Here $m_{\mathfrak{p}}(q_{2\mathrm{t}}) = 938.27209\;\mathrm{MeV}$ is the two-term categorical Lagrangian proton mass ([terminal resolution](#prop:terminal-resolution)) and $m_{\mathfrak{n}}(q_{2\mathrm{t}}) = m_{\mathfrak{p}}(q_{2\mathrm{t}}) + Q_\beta^{N=2,2\mathrm{t}}(q_{2\mathrm{t}}) + m_e = 939.56556\;\mathrm{MeV}$ is the derived neutron mass ($\delta m_{\mathfrak{n}\mathfrak{p}}^{\mathrm{QOU}} = 1.29347\;\mathrm{MeV}$); all MeV figures express dimensionless invariant ratios rendered against $m_e$.

**Derived aether constants at $q_0$.**

| Quantity | Algebraic expression | Value at $q_0$ |
|:---------|:---------------------|:--------------:|
| Quantum Planck quantum $\hbar_q$, Hecke step $h$ | $1 - q_0^{-1}$, $\;q_0 - q_0^{-1}$ | $0.09908$, $\;0.20906$ |
| Quantum integers $[2]_{q_0}$, $[3]_{q_0}$, $[4]_{q_0}$ | $(q_0^k - q_0^{-k})/(q_0 - q_0^{-1})$ | $2.01090$, $\;3.04371$, $\;4.10968$ |
| Bare Hecke scale $E_0$, Convention-D fugacity $z_D$ | $m_e/[q_0(q_0 - 1)]$, $\;q_0^3/(q_0^2 + 1)$ | $4.18598\;\mathrm{MeV}$, $\;0.61269$ |
| Two-, three-, four-body GPMT cumulants $(b_2, w_3, w_4^{(H_4)})$ | $E_0 \ln(1/z_D)$, $\;-E_0 d_{(1,1,1)}$, $\;E_0 \mu_4^{(H_4)}$ | $(+2.05071,\;+0.68392,\;-0.35289)\;\mathrm{MeV}$ |
| Temperley--Lieb singlet pairing gap $\Delta_{\mathrm{TL}}$ | $\tfrac{1}{2} w_3 [2]_{q_0}$ | $0.68765\;\mathrm{MeV}$ |
| Compton oscillator $E_{\mathrm{osc}}$, Fermi symmetry $a_{\mathrm{sym}}$ | $m_e/(q_0 - 1)^2$, $\;E_{\mathrm{osc}} z_D$ | $42.24777\;\mathrm{MeV}$, $\;25.88470\;\mathrm{MeV}$ |
| Spin--orbit strength $\kappa_{\mathrm{SO}}$, FCC Coulomb $a_{\mathrm{C}}^{\mathrm{FCC}}$ | $(q_0 - 1)^2$, $\;\tfrac{3}{5}\alpha_{\mathrm{EM}}(q_0)\hbar c / r_0^{\mathrm{FCC}}$ | $0.01210$, $\;0.73715\;\mathrm{MeV}$ |

For a compact simplicial 3-ball with $A \geq 4$ vertices, $f_0^\partial(A)$ boundary vertices ($f_0^\partial \propto A^{2/3}$), and $f_3(A)$ tetrahedra ($f_3(k) = 20k^3$ at Mackay shell $f_0(k) = (10k^3 + 15k^2 + 11k + 3)/3$, so $f_3 \sim 6A - O(A^{2/3})$), Euler--Dehn--Sommerville relations fix $f_1 = A + f_3 + f_0^\partial - 3$ and $f_2 = 2f_3 + f_0^\partial - 2$. Three-dimensional coordination thereby generates both linear volume saturation and $-A^{2/3}$ surface tension. Pauli promotion $E_{\mathrm{HO}}^{\mathrm{sym}}(A)$, Compton Fermi asymmetry $E_{\mathrm{sym}}^{\mathrm{F}}(Z, N) = a_{\mathrm{sym}}(N - Z)^2/A$, and Mayer--Jensen spin--orbit splitting $E_{\mathrm{SO}}(Z, N)$ establish the closures at $2, 8, 20, 28, 50, 82, 126$. Seniority pairing $\Delta_{\mathrm{TL}}(Z, N) \in \{+\Delta_{\mathrm{TL}}, 0, -\Delta_{\mathrm{TL}}\}$ and face-centered-cubic Wigner--Seitz Coulomb repulsion $E_{\mathrm{C}}^{\mathrm{FCC}}(Z, A) = a_{\mathrm{C}}^{\mathrm{FCC}} Z(Z - 1)A^{-1/3}$ ($r_0^{\mathrm{FCC}} = 1.17206\;\mathrm{fm}$) complete the Hamiltonian.

**Transfer-matrix scaling, electronic shells, and beta transitions.**

* **Factored nuclear skein product**: Pairwise crossings evaluate $P_{\mathcal{N}}(q) = \prod_{i=0}^{A-2} \hat{V}_i(q)$ ([Skein polynomial](#prop:skein-polynomial-transfer-matrix)) via $\binom{A}{2}$ $2 \times 2$ transfer-matrix multiplications ([transfer matrix operator](#def:transfer-matrix-operator)) of degree at most $A^2 - 1$, from $0$ steps on ${}^{1}\mathrm{H}$ and $1{,}540$ steps on ${}^{56}\mathrm{Fe}$ to $28{,}203$ steps on ${}^{238}\mathrm{U}$ and $43{,}071$ steps on ${}^{294}\mathrm{Og}$.
* **Electronic sub-shells**: Eigenvalues of the photon--electron transfer matrix $T_{\gamma e}(q_0)$ ([shell structure eigenvalues](#prop:shell-structure-eigenvalues)) with dominant root $\lambda_+ = 1.1073$ govern Rydberg scaling $\mathfrak{E}_{\mathrm{bind}} \propto \lambda_+^{-n}$ and tensor-product capacities $2, 6, 10, 14$ ($s, p, d, f$).
* **Isobaric beta transitions**: Beta decays shift crossing channels by the universal $2 \times 2$ perturbation $\Delta_\beta(q_0)$ ([beta decay matrix](#prop:beta-decay-transfer-matrix)). Because $\mathfrak{p}\text{--}\mathfrak{p}$ Coulomb repulsion grows as $Z(Z - 1)A^{-1/3}$ against Fermi asymmetry $a_{\mathrm{sym}}(N - Z)^2/A$ ([beta-stability](#prop:beta-stability)), stable heavy nuclei satisfy $N > Z$ beyond calcium, reaching $N = 176$ at ${}^{294}\mathrm{Og}$ ($Z = 118$).

## Complete 118-element knot-periodic table ($Z = 1\text{--}118$, $\mathrm{H}\text{--}\mathrm{Og}$)

All 118 IUPAC elements are tabulated across four nuclear shell periods using each element's canonical ground-state reference isotope in AME2020 (natural abundance standard for $Z \leq 92$ where primordial, longest-lived evaluated nuclide for synthetic $Z$). Every row is evaluated from the single unpatched closed-form functional $B_{\mathrm{QOU}}(Z, N)$ and $M_{\mathrm{QOU}}(Z, N)$ at 80 decimal digits with zero fitted parameters. Across the 117 bound elements ($Z = 2\text{--}118$), the median relative binding residual $|\Delta B/B|$ is $1.020\%$, with $|\Delta B/B| < 3.0\%$ on every element from $Z = 9$ fluorine through $Z = 118$ oganesson. Across $Z = 1\text{--}118$, the median neutral atomic mass residual $|\Delta M/M|$ is $87.9\;\mathrm{ppm}$ ($0.0088\%$). On ${}^{4}\mathrm{He}$ ($Z = 2$), the uniform single-crossing bulk shell lattice yields $3.611\;\mathrm{MeV}/A$, whereas the closed-shell $H_4(q_0)$ full-twist Wigner-singlet cell in the [recursive atom-knot atlas](#prop:recursive-atom-knot-atlas) captures intra-$\alpha$ double-twist pairing ($26.43\;\mathrm{MeV}$ bare, $6.606\;\mathrm{MeV}/A$).

All binding energies per nucleon $B/A$ and neutral atomic masses $M$ are in $\mathrm{MeV}$; $\diamond$ marks proton magic closures ($Z \in \{2, 8, 20, 28, 50, 82\}$) and $\star$ marks neutron magic closures ($N \in \{2, 8, 20, 28, 50, 82, 126\}$).

**Period I ($Z = 1\text{--}20$, $\mathrm{H}\text{--}\mathrm{Ca}$): harmonic-oscillator shells $N_{\mathrm{osc}} = 0, 1, 2$ (closures $Z = 2, 8, 20$).**

| $Z$ | Atom | $N$ | Cluster | $e^-$ shells | $B_{\mathrm{QOU}}/A$ | $B_{\mathrm{AME}}/A$ | $\Delta B/B$ | $M_{\mathrm{QOU}}$ | $M_{\mathrm{AME}}$ |
|---:|:---|---:|:---|:---|---:|---:|---:|---:|---:|
| 1 | ${}^{1}\mathrm{H}$ | 0 | $\mathfrak{p}$ | $1s^1$ | $0.000$ | $0.000$ | — | $938.78$ | $938.78$ |
| 2 | ${}^{4}\mathrm{He}^{\diamond\star}$ | 2 | $\alpha$ | $1s^2$ | $3.611$ | $7.074$ | $-48.95\%$ | $3742.25$ | $3728.40$ |
| 3 | ${}^{7}\mathrm{Li}$ | 4 | $\alpha{\oplus}\mathfrak{p}{\oplus}2\mathfrak{n}$ | $[\mathrm{He}]\,2s^1$ | $5.040$ | $5.606$ | $-10.10\%$ | $6539.33$ | $6535.37$ |
| 4 | ${}^{9}\mathrm{Be}$ | 5 | $2\alpha{\oplus}\mathfrak{n}$ | $[\mathrm{He}]\,2s^2$ | $5.858$ | $6.463$ | $-9.35\%$ | $8400.24$ | $8394.80$ |
| 5 | ${}^{11}\mathrm{B}$ | 6 | $2\alpha{\oplus}\mathfrak{p}{\oplus}2\mathfrak{n}$ | $[\mathrm{He}]\,2s^22p^1$ | $6.345$ | $6.928$ | $-8.42\%$ | $10261.52$ | $10255.10$ |
| 6 | ${}^{12}\mathrm{C}$ | 6 | $3\alpha$ | $[\mathrm{He}]\,2s^22p^2$ | $6.613$ | $7.680$ | $-13.89\%$ | $11190.73$ | $11177.93$ |
| 7 | ${}^{14}\mathrm{N}$ | 7 | $3\alpha{\oplus}\mathfrak{p}{\oplus}\mathfrak{n}$ | $[\mathrm{He}]\,2s^22p^3$ | $6.718$ | $7.476$ | $-10.13\%$ | $13054.38$ | $13043.78$ |
| 8 | ${}^{16}\mathrm{O}^{\diamond\star}$ | 8 | $4\alpha$ | $[\mathrm{He}]\,2s^22p^4$ | $7.495$ | $7.976$ | $-6.04\%$ | $14906.87$ | $14899.17$ |
| 9 | ${}^{19}\mathrm{F}$ | 10 | $4\alpha{\oplus}\mathfrak{p}{\oplus}2\mathfrak{n}$ | $[\mathrm{He}]\,2s^22p^5$ | $7.839$ | $7.779$ | $+0.77\%$ | $17695.77$ | $17696.90$ |
| 10 | ${}^{20}\mathrm{Ne}$ | 10 | $5\alpha$ | $[\mathrm{He}]\,2s^22p^6$ | $7.900$ | $8.032$ | $-1.65\%$ | $18625.49$ | $18622.84$ |
| 11 | ${}^{23}\mathrm{Na}$ | 12 | $5\alpha{\oplus}\mathfrak{p}{\oplus}2\mathfrak{n}$ | $[\mathrm{Ne}]\,3s^1$ | $8.152$ | $8.111$ | $+0.50\%$ | $21413.91$ | $21414.83$ |
| 12 | ${}^{24}\mathrm{Mg}$ | 12 | $6\alpha$ | $[\mathrm{Ne}]\,3s^2$ | $8.047$ | $8.261$ | $-2.58\%$ | $22347.04$ | $22341.93$ |
| 13 | ${}^{27}\mathrm{Al}$ | 14 | $6\alpha{\oplus}\mathfrak{p}{\oplus}2\mathfrak{n}$ | $[\mathrm{Ne}]\,3s^23p^1$ | $8.355$ | $8.332$ | $+0.28\%$ | $25132.52$ | $25133.14$ |
| 14 | ${}^{28}\mathrm{Si}$ | 14 | $7\alpha$ | $[\mathrm{Ne}]\,3s^23p^2$ | $8.345$ | $8.448$ | $-1.22\%$ | $26063.22$ | $26060.34$ |
| 15 | ${}^{31}\mathrm{P}$ | 16 | $7\alpha{\oplus}\mathfrak{p}{\oplus}2\mathfrak{n}$ | $[\mathrm{Ne}]\,3s^23p^3$ | $8.481$ | $8.481$ | $+0.00\%$ | $28851.89$ | $28851.88$ |
| 16 | ${}^{32}\mathrm{S}$ | 16 | $8\alpha$ | $[\mathrm{Ne}]\,3s^23p^4$ | $8.434$ | $8.493$ | $-0.69\%$ | $29783.68$ | $29781.80$ |
| 17 | ${}^{35}\mathrm{Cl}$ | 18 | $8\alpha{\oplus}\mathfrak{p}{\oplus}2\mathfrak{n}$ | $[\mathrm{Ne}]\,3s^23p^5$ | $8.526$ | $8.520$ | $+0.07\%$ | $32573.09$ | $32573.28$ |
| 18 | ${}^{40}\mathrm{Ar}$ | 22 | $9\alpha{\oplus}4\mathfrak{n}$ | $[\mathrm{Ne}]\,3s^23p^6$ | $8.710$ | $8.595$ | $+1.33\%$ | $37220.15$ | $37224.72$ |
| 19 | ${}^{39}\mathrm{K}^{\star}$ | 20 | $9\alpha{\oplus}\mathfrak{p}{\oplus}2\mathfrak{n}$ | $[\mathrm{Ar}]\,4s^1$ | $8.541$ | $8.557$ | $-0.19\%$ | $36295.09$ | $36294.46$ |
| 20 | ${}^{40}\mathrm{Ca}^{\diamond\star}$ | 20 | $10\alpha$ | $[\mathrm{Ar}]\,4s^2$ | $8.546$ | $8.551$ | $-0.06\%$ | $37225.13$ | $37224.92$ |

**Period II ($Z = 21\text{--}50$, $\mathrm{Sc}\text{--}\mathrm{Sn}$): spin--orbit intruder shells $1f_{7/2}$ ($Z = 28$) and $2p\text{--}1f_{5/2}\text{--}1g_{9/2}$ ($Z = 50$).**

| $Z$ | Atom | $N$ | Cluster | $e^-$ shells | $B_{\mathrm{QOU}}/A$ | $B_{\mathrm{AME}}/A$ | $\Delta B/B$ | $M_{\mathrm{QOU}}$ | $M_{\mathrm{AME}}$ |
|---:|:---|---:|:---|:---|---:|---:|---:|---:|---:|
| 21 | ${}^{45}\mathrm{Sc}$ | 24 | $10\alpha{\oplus}\mathfrak{p}{\oplus}4\mathfrak{n}$ | $[\mathrm{Ar}]\,3d^14s^2$ | $8.548$ | $8.619$ | $-0.82\%$ | $41879.36$ | $41876.16$ |
| 22 | ${}^{48}\mathrm{Ti}$ | 26 | $11\alpha{\oplus}4\mathfrak{n}$ | $[\mathrm{Ar}]\,3d^24s^2$ | $8.592$ | $8.723$ | $-1.51\%$ | $44669.54$ | $44663.22$ |
| 23 | ${}^{51}\mathrm{V}^{\star}$ | 28 | $11\alpha{\oplus}\mathfrak{p}{\oplus}6\mathfrak{n}$ | $[\mathrm{Ar}]\,3d^34s^2$ | $8.538$ | $8.742$ | $-2.33\%$ | $47464.40$ | $47454.00$ |
| 24 | ${}^{52}\mathrm{Cr}^{\star}$ | 28 | $12\alpha{\oplus}4\mathfrak{n}$ | $[\mathrm{Ar}]\,3d^54s^1$ | $8.543$ | $8.776$ | $-2.65\%$ | $48394.38$ | $48382.27$ |
| 25 | ${}^{55}\mathrm{Mn}$ | 30 | $12\alpha{\oplus}\mathfrak{p}{\oplus}6\mathfrak{n}$ | $[\mathrm{Ar}]\,3d^54s^2$ | $8.543$ | $8.765$ | $-2.53\%$ | $51186.67$ | $51174.46$ |
| 26 | ${}^{56}\mathrm{Fe}$ | 30 | $13\alpha{\oplus}4\mathfrak{n}$ | $[\mathrm{Ar}]\,3d^64s^2$ | $8.534$ | $8.790$ | $-2.91\%$ | $52117.41$ | $52103.06$ |
| 27 | ${}^{59}\mathrm{Co}$ | 32 | $13\alpha{\oplus}\mathfrak{p}{\oplus}6\mathfrak{n}$ | $[\mathrm{Ar}]\,3d^74s^2$ | $8.594$ | $8.768$ | $-1.99\%$ | $54906.21$ | $54895.92$ |
| 28 | ${}^{58}\mathrm{Ni}^{\diamond}$ | 30 | $14\alpha{\oplus}2\mathfrak{n}$ | $[\mathrm{Ar}]\,3d^84s^2$ | $8.473$ | $8.732$ | $-2.97\%$ | $53981.47$ | $53966.43$ |
| 29 | ${}^{63}\mathrm{Cu}$ | 34 | $14\alpha{\oplus}\mathfrak{p}{\oplus}6\mathfrak{n}$ | $[\mathrm{Ar}]\,3d^{10}4s^1$ | $8.663$ | $8.752$ | $-1.02\%$ | $58624.18$ | $58618.55$ |
| 30 | ${}^{64}\mathrm{Zn}$ | 34 | $15\alpha{\oplus}4\mathfrak{n}$ | $[\mathrm{Ar}]\,3d^{10}4s^2$ | $8.629$ | $8.736$ | $-1.22\%$ | $59556.44$ | $59549.62$ |
| 31 | ${}^{69}\mathrm{Ga}$ | 38 | $15\alpha{\oplus}\mathfrak{p}{\oplus}8\mathfrak{n}$ | $[\mathrm{Ar}]\,3d^{10}4s^24p^1$ | $8.691$ | $8.725$ | $-0.38\%$ | $64206.07$ | $64203.77$ |
| 32 | ${}^{74}\mathrm{Ge}$ | 42 | $16\alpha{\oplus}10\mathfrak{n}$ | $[\mathrm{Ar}]\,3d^{10}4s^24p^2$ | $8.762$ | $8.725$ | $+0.42\%$ | $68854.44$ | $68857.14$ |
| 33 | ${}^{75}\mathrm{As}$ | 42 | $16\alpha{\oplus}\mathfrak{p}{\oplus}10\mathfrak{n}$ | $[\mathrm{Ar}]\,3d^{10}4s^24p^3$ | $8.748$ | $8.701$ | $+0.54\%$ | $69785.51$ | $69789.02$ |
| 34 | ${}^{80}\mathrm{Se}$ | 46 | $17\alpha{\oplus}12\mathfrak{n}$ | $[\mathrm{Ar}]\,3d^{10}4s^24p^4$ | $8.790$ | $8.711$ | $+0.91\%$ | $74435.41$ | $74441.77$ |
| 35 | ${}^{79}\mathrm{Br}$ | 44 | $17\alpha{\oplus}\mathfrak{p}{\oplus}10\mathfrak{n}$ | $[\mathrm{Ar}]\,3d^{10}4s^24p^5$ | $8.826$ | $8.688$ | $+1.59\%$ | $73501.05$ | $73511.97$ |
| 36 | ${}^{84}\mathrm{Kr}$ | 48 | $18\alpha{\oplus}12\mathfrak{n}$ | $[\mathrm{Ar}]\,3d^{10}4s^24p^6$ | $8.756$ | $8.717$ | $+0.44\%$ | $78159.82$ | $78163.07$ |
| 37 | ${}^{85}\mathrm{Rb}$ | 48 | $18\alpha{\oplus}\mathfrak{p}{\oplus}12\mathfrak{n}$ | $[\mathrm{Kr}]\,5s^1$ | $8.763$ | $8.697$ | $+0.75\%$ | $79089.27$ | $79094.83$ |
| 38 | ${}^{88}\mathrm{Sr}^{\star}$ | 50 | $19\alpha{\oplus}12\mathfrak{n}$ | $[\mathrm{Kr}]\,5s^2$ | $8.752$ | $8.733$ | $+0.22\%$ | $81881.86$ | $81883.56$ |
| 39 | ${}^{89}\mathrm{Y}^{\star}$ | 50 | $19\alpha{\oplus}\mathfrak{p}{\oplus}12\mathfrak{n}$ | $[\mathrm{Kr}]\,4d^15s^2$ | $8.752$ | $8.714$ | $+0.43\%$ | $82811.92$ | $82815.26$ |
| 40 | ${}^{90}\mathrm{Zr}^{\star}$ | 50 | $20\alpha{\oplus}10\mathfrak{n}$ | $[\mathrm{Kr}]\,4d^25s^2$ | $8.756$ | $8.710$ | $+0.53\%$ | $83741.57$ | $83745.70$ |
| 41 | ${}^{93}\mathrm{Nb}$ | 52 | $20\alpha{\oplus}\mathfrak{p}{\oplus}12\mathfrak{n}$ | $[\mathrm{Kr}]\,4d^45s^1$ | $8.695$ | $8.664$ | $+0.36\%$ | $86538.87$ | $86541.74$ |
| 42 | ${}^{98}\mathrm{Mo}$ | 56 | $21\alpha{\oplus}14\mathfrak{n}$ | $[\mathrm{Kr}]\,4d^55s^1$ | $8.675$ | $8.635$ | $+0.46\%$ | $91194.39$ | $91198.31$ |
| 43 | ${}^{98}\mathrm{Tc}$ | 55 | $21\alpha{\oplus}\mathfrak{p}{\oplus}13\mathfrak{n}$ | $[\mathrm{Kr}]\,4d^55s^2$ | $8.670$ | $8.610$ | $+0.69\%$ | $91194.16$ | $91199.99$ |
| 44 | ${}^{102}\mathrm{Ru}$ | 58 | $22\alpha{\oplus}14\mathfrak{n}$ | $[\mathrm{Kr}]\,4d^75s^1$ | $8.661$ | $8.607$ | $+0.62\%$ | $94917.88$ | $94923.29$ |
| 45 | ${}^{103}\mathrm{Rh}$ | 58 | $22\alpha{\oplus}\mathfrak{p}{\oplus}14\mathfrak{n}$ | $[\mathrm{Kr}]\,4d^85s^1$ | $8.656$ | $8.584$ | $+0.84\%$ | $95848.47$ | $95855.86$ |
| 46 | ${}^{106}\mathrm{Pd}$ | 60 | $23\alpha{\oplus}14\mathfrak{n}$ | $[\mathrm{Kr}]\,4d^{10}$ | $8.619$ | $8.580$ | $+0.46\%$ | $98644.32$ | $98648.47$ |
| 47 | ${}^{107}\mathrm{Ag}$ | 60 | $23\alpha{\oplus}\mathfrak{p}{\oplus}14\mathfrak{n}$ | $[\mathrm{Kr}]\,4d^{10}5s^1$ | $8.609$ | $8.554$ | $+0.65\%$ | $99575.56$ | $99581.46$ |
| 48 | ${}^{114}\mathrm{Cd}$ | 66 | $24\alpha{\oplus}18\mathfrak{n}$ | $[\mathrm{Kr}]\,4d^{10}5s^2$ | $8.575$ | $8.532$ | $+0.51\%$ | $106095.38$ | $106100.31$ |
| 49 | ${}^{115}\mathrm{In}$ | 66 | $24\alpha{\oplus}\mathfrak{p}{\oplus}18\mathfrak{n}$ | $[\mathrm{Kr}]\,4d^{10}5s^25p^1$ | $8.554$ | $8.517$ | $+0.44\%$ | $107028.01$ | $107032.29$ |
| 50 | ${}^{120}\mathrm{Sn}^{\diamond}$ | 70 | $25\alpha{\oplus}20\mathfrak{n}$ | $[\mathrm{Kr}]\,4d^{10}5s^25p^2$ | $8.526$ | $8.504$ | $+0.25\%$ | $111685.63$ | $111688.20$ |

**Period III ($Z = 51\text{--}82$, $\mathrm{Sb}\text{--}\mathrm{Pb}$): $N_{\mathrm{osc}} = 4$ and $1h_{11/2}$ intruder shell (closure $Z = 82$).**

| $Z$ | Atom | $N$ | Cluster | $e^-$ shells | $B_{\mathrm{QOU}}/A$ | $B_{\mathrm{AME}}/A$ | $\Delta B/B$ | $M_{\mathrm{QOU}}$ | $M_{\mathrm{AME}}$ |
|---:|:---|---:|:---|:---|---:|---:|---:|---:|---:|
| 51 | ${}^{121}\mathrm{Sb}$ | 70 | $25\alpha{\oplus}\mathfrak{p}{\oplus}20\mathfrak{n}$ | $[\mathrm{Kr}]\,4d^{10}5s^25p^3$ | $8.504$ | $8.482$ | $+0.26\%$ | $112618.49$ | $112621.19$ |
| 52 | ${}^{130}\mathrm{Te}$ | 78 | $26\alpha{\oplus}26\mathfrak{n}$ | $[\mathrm{Kr}]\,4d^{10}5s^25p^4$ | $8.392$ | $8.430$ | $-0.45\%$ | $121011.84$ | $121006.88$ |
| 53 | ${}^{127}\mathrm{I}$ | 74 | $26\alpha{\oplus}\mathfrak{p}{\oplus}22\mathfrak{n}$ | $[\mathrm{Kr}]\,4d^{10}5s^25p^5$ | $8.483$ | $8.445$ | $+0.44\%$ | $118206.04$ | $118210.77$ |
| 54 | ${}^{132}\mathrm{Xe}$ | 78 | $27\alpha{\oplus}24\mathfrak{n}$ | $[\mathrm{Kr}]\,4d^{10}5s^25p^6$ | $8.433$ | $8.428$ | $+0.06\%$ | $122867.31$ | $122867.94$ |
| 55 | ${}^{133}\mathrm{Cs}$ | 78 | $27\alpha{\oplus}\mathfrak{p}{\oplus}24\mathfrak{n}$ | $[\mathrm{Xe}]\,6s^1$ | $8.437$ | $8.410$ | $+0.32\%$ | $123797.04$ | $123800.65$ |
| 56 | ${}^{138}\mathrm{Ba}^{\star}$ | 82 | $28\alpha{\oplus}26\mathfrak{n}$ | $[\mathrm{Xe}]\,6s^2$ | $8.383$ | $8.393$ | $-0.13\%$ | $128459.44$ | $128457.93$ |
| 57 | ${}^{139}\mathrm{La}^{\star}$ | 82 | $28\alpha{\oplus}\mathfrak{p}{\oplus}26\mathfrak{n}$ | $[\mathrm{Xe}]\,5d^16s^2$ | $8.369$ | $8.378$ | $-0.11\%$ | $129391.77$ | $129390.46$ |
| 58 | ${}^{140}\mathrm{Ce}^{\star}$ | 82 | $29\alpha{\oplus}24\mathfrak{n}$ | $[\mathrm{Xe}]\,4f^15d^16s^2$ | $8.401$ | $8.376$ | $+0.30\%$ | $130317.65$ | $130321.10$ |
| 59 | ${}^{141}\mathrm{Pr}^{\star}$ | 82 | $29\alpha{\oplus}\mathfrak{p}{\oplus}24\mathfrak{n}$ | $[\mathrm{Xe}]\,4f^36s^2$ | $8.374$ | $8.354$ | $+0.24\%$ | $131251.86$ | $131254.65$ |
| 60 | ${}^{142}\mathrm{Nd}^{\star}$ | 82 | $30\alpha{\oplus}22\mathfrak{n}$ | $[\mathrm{Xe}]\,4f^46s^2$ | $8.371$ | $8.346$ | $+0.30\%$ | $132182.67$ | $132186.21$ |
| 61 | ${}^{145}\mathrm{Pm}$ | 84 | $30\alpha{\oplus}\mathfrak{p}{\oplus}24\mathfrak{n}$ | $[\mathrm{Xe}]\,4f^56s^2$ | $8.304$ | $8.303$ | $+0.01\%$ | $134985.25$ | $134985.38$ |
| 62 | ${}^{152}\mathrm{Sm}$ | 90 | $31\alpha{\oplus}28\mathfrak{n}$ | $[\mathrm{Xe}]\,4f^66s^2$ | $8.246$ | $8.244$ | $+0.03\%$ | $141512.01$ | $141512.34$ |
| 63 | ${}^{153}\mathrm{Eu}$ | 90 | $31\alpha{\oplus}\mathfrak{p}{\oplus}28\mathfrak{n}$ | $[\mathrm{Xe}]\,4f^76s^2$ | $8.244$ | $8.229$ | $+0.19\%$ | $142442.87$ | $142445.23$ |
| 64 | ${}^{158}\mathrm{Gd}$ | 94 | $32\alpha{\oplus}30\mathfrak{n}$ | $[\mathrm{Xe}]\,4f^75d^16s^2$ | $8.210$ | $8.202$ | $+0.10\%$ | $147104.06$ | $147105.38$ |
| 65 | ${}^{159}\mathrm{Tb}$ | 94 | $32\alpha{\oplus}\mathfrak{p}{\oplus}30\mathfrak{n}$ | $[\mathrm{Xe}]\,4f^96s^2$ | $8.205$ | $8.189$ | $+0.20\%$ | $148035.40$ | $148038.03$ |
| 66 | ${}^{164}\mathrm{Dy}$ | 98 | $33\alpha{\oplus}32\mathfrak{n}$ | $[\mathrm{Xe}]\,4f^{10}6s^2$ | $8.174$ | $8.159$ | $+0.19\%$ | $152696.53$ | $152699.07$ |
| 67 | ${}^{165}\mathrm{Ho}$ | 98 | $33\alpha{\oplus}\mathfrak{p}{\oplus}32\mathfrak{n}$ | $[\mathrm{Xe}]\,4f^{11}6s^2$ | $8.172$ | $8.147$ | $+0.31\%$ | $153627.46$ | $153631.63$ |
| 68 | ${}^{166}\mathrm{Er}$ | 98 | $34\alpha{\oplus}30\mathfrak{n}$ | $[\mathrm{Xe}]\,4f^{12}6s^2$ | $8.173$ | $8.142$ | $+0.38\%$ | $154557.98$ | $154563.10$ |
| 69 | ${}^{169}\mathrm{Tm}$ | 100 | $34\alpha{\oplus}\mathfrak{p}{\oplus}32\mathfrak{n}$ | $[\mathrm{Xe}]\,4f^{13}6s^2$ | $8.153$ | $8.114$ | $+0.48\%$ | $157354.70$ | $157361.23$ |
| 70 | ${}^{174}\mathrm{Yb}$ | 104 | $35\alpha{\oplus}34\mathfrak{n}$ | $[\mathrm{Xe}]\,4f^{14}6s^2$ | $8.118$ | $8.084$ | $+0.42\%$ | $162017.17$ | $162023.03$ |
| 71 | ${}^{175}\mathrm{Lu}$ | 104 | $35\alpha{\oplus}\mathfrak{p}{\oplus}34\mathfrak{n}$ | $[\mathrm{Xe}]\,4f^{14}5d^16s^2$ | $8.113$ | $8.069$ | $+0.55\%$ | $162948.59$ | $162956.30$ |
| 72 | ${}^{180}\mathrm{Hf}$ | 108 | $36\alpha{\oplus}36\mathfrak{n}$ | $[\mathrm{Xe}]\,4f^{14}5d^26s^2$ | $8.081$ | $8.035$ | $+0.58\%$ | $167610.85$ | $167619.16$ |
| 73 | ${}^{181}\mathrm{Ta}$ | 108 | $36\alpha{\oplus}\mathfrak{p}{\oplus}36\mathfrak{n}$ | $[\mathrm{Xe}]\,4f^{14}5d^36s^2$ | $8.079$ | $8.023$ | $+0.70\%$ | $168541.91$ | $168551.99$ |
| 74 | ${}^{184}\mathrm{W}$ | 110 | $37\alpha{\oplus}36\mathfrak{n}$ | $[\mathrm{Xe}]\,4f^{14}5d^46s^2$ | $8.067$ | $8.005$ | $+0.77\%$ | $171337.82$ | $171349.21$ |
| 75 | ${}^{187}\mathrm{Re}$ | 112 | $37\alpha{\oplus}\mathfrak{p}{\oplus}38\mathfrak{n}$ | $[\mathrm{Xe}]\,4f^{14}5d^56s^2$ | $8.044$ | $7.978$ | $+0.83\%$ | $174135.85$ | $174148.18$ |
| 76 | ${}^{192}\mathrm{Os}$ | 116 | $38\alpha{\oplus}40\mathfrak{n}$ | $[\mathrm{Xe}]\,4f^{14}5d^66s^2$ | $8.018$ | $7.949$ | $+0.87\%$ | $178797.69$ | $178810.99$ |
| 77 | ${}^{193}\mathrm{Ir}$ | 116 | $38\alpha{\oplus}\mathfrak{p}{\oplus}40\mathfrak{n}$ | $[\mathrm{Xe}]\,4f^{14}5d^76s^2$ | $8.016$ | $7.938$ | $+0.99\%$ | $179728.74$ | $179743.83$ |
| 78 | ${}^{195}\mathrm{Pt}$ | 117 | $39\alpha{\oplus}39\mathfrak{n}$ | $[\mathrm{Xe}]\,4f^{14}5d^96s^1$ | $8.008$ | $7.927$ | $+1.03\%$ | $181592.60$ | $181608.56$ |
| 79 | ${}^{197}\mathrm{Au}$ | 118 | $39\alpha{\oplus}\mathfrak{p}{\oplus}40\mathfrak{n}$ | $[\mathrm{Xe}]\,4f^{14}5d^{10}6s^1$ | $8.000$ | $7.916$ | $+1.06\%$ | $183456.64$ | $183473.20$ |
| 80 | ${}^{202}\mathrm{Hg}$ | 122 | $40\alpha{\oplus}42\mathfrak{n}$ | $[\mathrm{Xe}]\,4f^{14}5d^{10}6s^2$ | $7.975$ | $7.897$ | $+0.99\%$ | $188118.63$ | $188134.46$ |
| 81 | ${}^{205}\mathrm{Tl}$ | 124 | $40\alpha{\oplus}\mathfrak{p}{\oplus}44\mathfrak{n}$ | $[\mathrm{Xe}]\,4f^{14}5d^{10}6s^26p^1$ | $7.956$ | $7.878$ | $+0.98\%$ | $190916.64$ | $190932.47$ |
| 82 | ${}^{208}\mathrm{Pb}^{\diamond\star}$ | 126 | $41\alpha{\oplus}44\mathfrak{n}$ | $[\mathrm{Xe}]\,4f^{14}5d^{10}6s^26p^2$ | $7.944$ | $7.867$ | $+0.98\%$ | $193713.06$ | $193729.03$ |

**Period IV ($Z = 83\text{--}118$, $\mathrm{Bi}\text{--}\mathrm{Og}$): actinide and transactinide $N_{\mathrm{osc}} = 5$ and $1i_{13/2}$ shell toward $Z = 126$.**

| $Z$ | Atom | $N$ | Cluster | $e^-$ shells | $B_{\mathrm{QOU}}/A$ | $B_{\mathrm{AME}}/A$ | $\Delta B/B$ | $M_{\mathrm{QOU}}$ | $M_{\mathrm{AME}}$ |
|---:|:---|---:|:---|:---|---:|---:|---:|---:|---:|
| 83 | ${}^{209}\mathrm{Bi}^{\star}$ | 126 | $41\alpha{\oplus}\mathfrak{p}{\oplus}44\mathfrak{n}$ | $[\mathrm{Xe}]\,4f^{14}5d^{10}6s^26p^3$ | $7.938$ | $7.848$ | $+1.15\%$ | $194645.23$ | $194664.01$ |
| 84 | ${}^{209}\mathrm{Po}$ | 125 | $42\alpha{\oplus}41\mathfrak{n}$ | $[\mathrm{Xe}]\,4f^{14}5d^{10}6s^26p^4$ | $7.936$ | $7.835$ | $+1.29\%$ | $194644.80$ | $194665.90$ |
| 85 | ${}^{210}\mathrm{At}$ | 125 | $42\alpha{\oplus}\mathfrak{p}{\oplus}41\mathfrak{n}$ | $[\mathrm{Xe}]\,4f^{14}5d^{10}6s^26p^5$ | $7.922$ | $7.812$ | $+1.41\%$ | $195578.65$ | $195601.79$ |
| 86 | ${}^{222}\mathrm{Rn}$ | 136 | $43\alpha{\oplus}50\mathfrak{n}$ | $[\mathrm{Xe}]\,4f^{14}5d^{10}6s^26p^6$ | $7.853$ | $7.694$ | $+2.06\%$ | $206772.96$ | $206808.06$ |
| 87 | ${}^{223}\mathrm{Fr}$ | 136 | $43\alpha{\oplus}\mathfrak{p}{\oplus}50\mathfrak{n}$ | $[\mathrm{Rn}]\,7s^1$ | $7.849$ | $7.684$ | $+2.15\%$ | $207704.70$ | $207741.57$ |
| 88 | ${}^{226}\mathrm{Ra}$ | 138 | $44\alpha{\oplus}50\mathfrak{n}$ | $[\mathrm{Rn}]\,7s^2$ | $7.826$ | $7.662$ | $+2.14\%$ | $210504.35$ | $210541.34$ |
| 89 | ${}^{227}\mathrm{Ac}$ | 138 | $44\alpha{\oplus}\mathfrak{p}{\oplus}50\mathfrak{n}$ | $[\mathrm{Rn}]\,6d^17s^2$ | $7.817$ | $7.651$ | $+2.17\%$ | $211437.32$ | $211475.01$ |
| 90 | ${}^{232}\mathrm{Th}$ | 142 | $45\alpha{\oplus}52\mathfrak{n}$ | $[\mathrm{Rn}]\,6d^27s^2$ | $7.771$ | $7.615$ | $+2.04\%$ | $216105.99$ | $216142.08$ |
| 91 | ${}^{231}\mathrm{Pa}$ | 140 | $45\alpha{\oplus}\mathfrak{p}{\oplus}50\mathfrak{n}$ | $[\mathrm{Rn}]\,5f^26d^17s^2$ | $7.780$ | $7.618$ | $+2.12\%$ | $215171.28$ | $215208.56$ |
| 92 | ${}^{238}\mathrm{U}$ | 146 | $46\alpha{\oplus}54\mathfrak{n}$ | $[\mathrm{Rn}]\,5f^36d^17s^2$ | $7.709$ | $7.570$ | $+1.83\%$ | $221709.88$ | $221742.91$ |
| 93 | ${}^{237}\mathrm{Np}$ | 144 | $46\alpha{\oplus}\mathfrak{p}{\oplus}52\mathfrak{n}$ | $[\mathrm{Rn}]\,5f^46d^17s^2$ | $7.724$ | $7.575$ | $+1.97\%$ | $220773.60$ | $220808.98$ |
| 94 | ${}^{244}\mathrm{Pu}$ | 150 | $47\alpha{\oplus}56\mathfrak{n}$ | $[\mathrm{Rn}]\,5f^67s^2$ | $7.653$ | $7.525$ | $+1.71\%$ | $227313.00$ | $227344.37$ |
| 95 | ${}^{243}\mathrm{Am}$ | 148 | $47\alpha{\oplus}\mathfrak{p}{\oplus}54\mathfrak{n}$ | $[\mathrm{Rn}]\,5f^77s^2$ | $7.667$ | $7.530$ | $+1.82\%$ | $226376.99$ | $226410.24$ |
| 96 | ${}^{247}\mathrm{Cm}$ | 151 | $48\alpha{\oplus}55\mathfrak{n}$ | $[\mathrm{Rn}]\,5f^76d^17s^2$ | $7.628$ | $7.502$ | $+1.69\%$ | $230113.34$ | $230144.58$ |
| 97 | ${}^{247}\mathrm{Bk}$ | 150 | $48\alpha{\oplus}\mathfrak{p}{\oplus}54\mathfrak{n}$ | $[\mathrm{Rn}]\,5f^97s^2$ | $7.631$ | $7.499$ | $+1.75\%$ | $230112.05$ | $230144.53$ |
| 98 | ${}^{251}\mathrm{Cf}$ | 153 | $49\alpha{\oplus}55\mathfrak{n}$ | $[\mathrm{Rn}]\,5f^{10}7s^2$ | $7.595$ | $7.471$ | $+1.66\%$ | $233847.99$ | $233879.16$ |
| 99 | ${}^{252}\mathrm{Es}$ | 153 | $49\alpha{\oplus}\mathfrak{p}{\oplus}55\mathfrak{n}$ | $[\mathrm{Rn}]\,5f^{11}7s^2$ | $7.582$ | $7.457$ | $+1.68\%$ | $234782.35$ | $234813.81$ |
| 100 | ${}^{257}\mathrm{Fm}$ | 157 | $50\alpha{\oplus}57\mathfrak{n}$ | $[\mathrm{Rn}]\,5f^{12}7s^2$ | $7.541$ | $7.422$ | $+1.61\%$ | $239451.97$ | $239482.58$ |
| 101 | ${}^{258}\mathrm{Md}$ | 157 | $50\alpha{\oplus}\mathfrak{p}{\oplus}57\mathfrak{n}$ | $[\mathrm{Rn}]\,5f^{13}7s^2$ | $7.529$ | $7.410$ | $+1.61\%$ | $240386.36$ | $240417.17$ |
| 102 | ${}^{259}\mathrm{No}$ | 157 | $51\alpha{\oplus}55\mathfrak{n}$ | $[\mathrm{Rn}]\,5f^{14}7s^2$ | $7.519$ | $7.400$ | $+1.61\%$ | $241320.18$ | $241351.05$ |
| 103 | ${}^{266}\mathrm{Lr}$ | 163 | $51\alpha{\oplus}\mathfrak{p}{\oplus}61\mathfrak{n}$ | $[\mathrm{Rn}]\,5f^{14}7s^27p^1$ | $7.459$ | $7.349$ | $+1.50\%$ | $247859.68$ | $247888.99$ |
| 104 | ${}^{267}\mathrm{Rf}$ | 163 | $52\alpha{\oplus}59\mathfrak{n}$ | $[\mathrm{Rn}]\,5f^{14}6d^27s^2$ | $7.453$ | $7.342$ | $+1.51\%$ | $248792.81$ | $248822.29$ |
| 105 | ${}^{268}\mathrm{Db}$ | 163 | $52\alpha{\oplus}\mathfrak{p}{\oplus}59\mathfrak{n}$ | $[\mathrm{Rn}]\,5f^{14}6d^37s^2$ | $7.438$ | $7.328$ | $+1.50\%$ | $249728.10$ | $249757.48$ |
| 106 | ${}^{269}\mathrm{Sg}$ | 163 | $53\alpha{\oplus}57\mathfrak{n}$ | $[\mathrm{Rn}]\,5f^{14}6d^47s^2$ | $7.428$ | $7.318$ | $+1.50\%$ | $250662.14$ | $250691.63$ |
| 107 | ${}^{270}\mathrm{Bh}$ | 163 | $53\alpha{\oplus}\mathfrak{p}{\oplus}57\mathfrak{n}$ | $[\mathrm{Rn}]\,5f^{14}6d^57s^2$ | $7.411$ | $7.301$ | $+1.50\%$ | $251598.14$ | $251627.68$ |
| 108 | ${}^{270}\mathrm{Hs}$ | 162 | $54\alpha{\oplus}54\mathfrak{n}$ | $[\mathrm{Rn}]\,5f^{14}6d^67s^2$ | $7.403$ | $7.295$ | $+1.49\%$ | $251599.25$ | $251628.52$ |
| 109 | ${}^{278}\mathrm{Mt}$ | 169 | $54\alpha{\oplus}\mathfrak{p}{\oplus}61\mathfrak{n}$ | $[\mathrm{Rn}]\,5f^{14}6d^77s^2$ | $7.354$ | $7.240$ | $+1.57\%$ | $259069.56$ | $259101.19$ |
| 110 | ${}^{281}\mathrm{Ds}$ | 171 | $55\alpha{\oplus}61\mathfrak{n}$ | $[\mathrm{Rn}]\,5f^{14}6d^87s^2$ | $7.336$ | $7.220$ | $+1.60\%$ | $261870.56$ | $261903.01$ |
| 111 | ${}^{282}\mathrm{Rg}$ | 171 | $55\alpha{\oplus}\mathfrak{p}{\oplus}61\mathfrak{n}$ | $[\mathrm{Rn}]\,5f^{14}6d^97s^2$ | $7.319$ | $7.204$ | $+1.59\%$ | $262806.81$ | $262839.08$ |
| 112 | ${}^{285}\mathrm{Cn}$ | 173 | $56\alpha{\oplus}61\mathfrak{n}$ | $[\mathrm{Rn}]\,5f^{14}6d^{10}7s^2$ | $7.300$ | $7.185$ | $+1.60\%$ | $265608.07$ | $265640.80$ |
| 113 | ${}^{286}\mathrm{Nh}$ | 173 | $56\alpha{\oplus}\mathfrak{p}{\oplus}61\mathfrak{n}$ | $[\mathrm{Rn}]\,5f^{14}6d^{10}7s^27p^1$ | $7.283$ | $7.168$ | $+1.60\%$ | $266544.47$ | $266577.26$ |
| 114 | ${}^{289}\mathrm{Fl}$ | 175 | $57\alpha{\oplus}61\mathfrak{n}$ | $[\mathrm{Rn}]\,5f^{14}6d^{10}7s^27p^2$ | $7.265$ | $7.149$ | $+1.63\%$ | $269345.55$ | $269379.16$ |
| 115 | ${}^{290}\mathrm{Mc}$ | 175 | $57\alpha{\oplus}\mathfrak{p}{\oplus}61\mathfrak{n}$ | $[\mathrm{Rn}]\,5f^{14}6d^{10}7s^27p^3$ | $7.248$ | $7.131$ | $+1.64\%$ | $270282.09$ | $270316.01$ |
| 116 | ${}^{293}\mathrm{Lv}$ | 177 | $58\alpha{\oplus}61\mathfrak{n}$ | $[\mathrm{Rn}]\,5f^{14}6d^{10}7s^27p^4$ | $7.230$ | $7.111$ | $+1.67\%$ | $273083.63$ | $273118.39$ |
| 117 | ${}^{294}\mathrm{Ts}$ | 177 | $58\alpha{\oplus}\mathfrak{p}{\oplus}61\mathfrak{n}$ | $[\mathrm{Rn}]\,5f^{14}6d^{10}7s^27p^5$ | $7.211$ | $7.092$ | $+1.68\%$ | $274020.63$ | $274055.65$ |
| 118 | ${}^{294}\mathrm{Og}$ | 176 | $59\alpha{\oplus}58\mathfrak{n}$ | $[\mathrm{Rn}]\,5f^{14}6d^{10}7s^27p^6$ | $7.198$ | $7.079$ | $+1.68\%$ | $274023.68$ | $274058.69$ |

**Knot exhaustiveness and building-block reference.**

Irreducible summand detection is complete via Alexander surjectivity and Markov non-degeneracy ([knot exhaustiveness](#rem:knot-exhaustiveness)), and generation over Seifert genus at most $4$ is complete ([generation completeness](#thm:generation-completeness)). Jones faithfulness is not invoked because Jones evaluation serves detection rather than classification. Constituent Jones polynomials and hyperbolic volumes are catalogued in [building-block knots](#rem:building-block-knots), while the multi-level hierarchy across all $3{,}558$ AME2020 nuclides appears in the [recursive atom-knot atlas](#prop:recursive-atom-knot-atlas) and [atlas registry](#rem:recursive-atom-knot-atlas-registry).
