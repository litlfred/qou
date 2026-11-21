*The covalent bond word is selected by the same rule as every other canonical word: $\gamma\gamma$ construction followed by reading-3 confinement. Write $V_s = \sigma_s \sigma_{s+1}^{-1}$ for the pair-production unit. The $H_2$ word lives on twelve strands: each atom is a nucleon word $V^m$ and an electron word $V^k$ on its own three-strand windows, and a bond letter $K$ sits at a junction site $s \in \{4, 5\}$ between the two atoms. Reading 3 asks $\chi_\lambda \geq 0$ on every block with $y_\lambda > 0$ under convention D, at every level $1, \dots, 12$.*

*Proposition. Let the nucleon be $V^m$ with $m \in \{3, 6\}$ and the electron $V^k$ with $k \in \{0, 3, 6\}$, the powers that pass reading 3 on their own three strands. At the proton pin $q = q_0 \approx 1.10998$, among the bond letters restricted to the powers $K \in \{V_s, V_s^2, V_s^3\}$ at $s \in \{4, 5\}$, the bonded $H_2$ word passes reading 3 exactly for $K = V_s^3$, at either site. The uniqueness is a statement about this family of powers only; it does not hold for the full term alphabet of the photon (see the remark below).*

### Why the inverse trefoil is excluded

An earlier selection took the minimum-crossing knot from a list of knots and obtained the inverse trefoil $T_{2,3}^{-1} = \sigma_0^{-1}\sigma_1^{-1}\sigma_0^{-1}$. Every $\gamma\gamma$ word has even length, since each vertex contributes two letters, and the inverse trefoil has three. So it is not a $\gamma\gamma$ word and cannot be the bond word under the one rule.

### Scope

The result is a finite computation at a single value of $q$, the proton pin $q_0$, where every character is evaluated in 40-digit arithmetic. No other value of $q$ is tested, and $q_0$ is fixed by calibration, so the proposition is a statement about that one point. The computation covers nucleon powers $m \leq 6$, electron powers $k \leq 7$, bond powers at most $3$, the configuration with no proton–electron letter and no junction letter, both atom orders. Bond powers above $3$ are not tested.

The hypothesis on the electron carries the uniqueness. If the electron is a $\gamma\gamma$ power that fails reading 3 on its own strands ($k \in \{1, 2, 4, 5, 7\}$), the bonded word can still pass with $K = V_4$ or $K = V_4^2$: the bond repairs a constituent that fails alone. Read with reading 3 applied to the bonded word only, the cheapest such state ($m = 3$, $k = 1$, $K = V_4$, 18 crossings) ties in crossing count with the cheapest $V^3$-bonded state ($m = 3$, $k = 0$, $K = V_4^3$). Whether the constituents of a bonded group must also pass alone is therefore part of the selection rule, not a consequence of it. The selection rule requires it: every particle must pass reading 3 on its own strands as well as inside the bonded word. Under that rule the hypothesis on the electron holds and $K = V_s^3$ is the unique bond. The same holds outside the $\gamma\gamma$ electron grammar: with a stabilised torus electron $T(2,m)$, the $V_s$ and $V_s^2$ bonds also pass in some configurations. The proposition is stated only for electrons $V^k$, $k \in \{0, 3, 6\}$.

### Remark: the electron $\sigma_0\sigma_1\sigma_0$ and the photon's term alphabet

The electron is now the word $E = \sigma_0\sigma_1\sigma_0 \in B_3$, whose closure is the Hopf link, and the photon is $\gamma = 1 + \varphi_0\sigma_0 + \varphi_1\sigma_1 + \varphi_{01}\sigma_0\sigma_1^{-1}$. Neither changes the proposition: with $E$ in place of $V^k$, the powers $V_s^k$ ($k = 1, 2, 3$) reproduce the rows above exactly, and only $V_s^3$ passes.

The photon, however, offers more bond letters than the powers of $V_s$. A photon absorbed at a junction window contributes one non-identity term of $\gamma_s$, so the letters at the windows $s \in \{4, 5\}$ are $\sigma_4, \sigma_5, \sigma_6, V_4, V_5$. A computation fixed in advance tested every product of one, two or three of these letters, 155 bonds in all, each monomial on its own so that no value of $\varphi$ is chosen. Its findings, at $q_0$ with nucleons $V^3$ and $V^6$ and both atom orders:

1. The electron $E$ passes reading 3 on its own strands, but only with equality: its character on the block $(2,1)$ is $0$ for every $q$, since $\chi_{(2,1)}(\sigma_0\sigma_1\sigma_0) = -(q - q^{-1}) + (q - q^{-1}) = 0$. The bare $H_2$ word passes.
2. No single photon term that crosses the cut between the atoms passes. Of the 155 bonds, 37 pass in the order $pe$ and 32 in the order $ep$; 30 and 25 of these cross the cut. So $V_s^3$ is not unique in the full alphabet.
3. The passing cut-crossing bond with fewest crossings is $\sigma_5^2$: two photons, two crossings, a pure braid clasping the electron of the first atom to the first strand of the second. Its trace ratio is $1.12809$, so the trace increases, while for $V_s^3$ it is $0.997$ to $1.0$.
4. With the two-term trace, whose lepton insertion depends only on the total weight and the numbers of quark and lepton strands, the connected term vanishes on every word, so every result above is the same under the one-term and the two-term trace. This uses the strand charges $Q = T^3 + 1/6$ on quark strands and $Q = T^3 - 1/2$ on lepton strands, which are an assumption here.

The selection rule as it stands does not choose among the passing bonds. A rule by fewest crossings would select $\sigma_5^2$; a rule requiring the trace to fall would exclude it. Neither rule is part of the present selection, so the bond under the full photon alphabet is left open.

### Trace

The Markov trace of the bonded word over the bare word is reported, not used for selection: $0.9984$ to $0.9986$ for every $V^3$ bond above. The binding energy formerly quoted for $H_2$ was computed on the inverse trefoil word and does not carry over to the $\gamma\gamma$ bond.
