**Theorem (conditional on [Stokes DT BPS bridge conjecture](#conj:stokes-dt-bps-bridge)).**
Under the closed-sector Stokes--DT--BPS bridge, the G3 Stokes integer of the
figure-eight $4_1$ is a BPS/DT count:

$$
  A_\omega(4_1) \;=\; \dim \mathcal{H}_{\mathrm{BPS}}\big(T[4_1]\big) \;=\; 3 .
$$

### Derivation (through the bridge)

The bridge supplies two identifications, valid for every knot $K$:

$$
  \mathfrak{S}(K) \;\overset{\text{GGM 3(d)}}{=}\; \Omega_{\mathrm{DT}}(K)
  \;\overset{\text{GPPV}}{=}\; \dim \mathcal{H}_{\mathrm{BPS}}(T[K]) .
$$

Specialise to $K = 4_1$ and feed the **bridge-independent, certified** Stokes
datum: the Garoufalidis--Gu--Mariño eq-(60) $q \to 0$ off-diagonal of the $4_1$
Stokes matrix is $\mathfrak{S}(4_1) = S^+(0)_{01} = 3$, proved unconditionally by
decidable integer-matrix algebra from the certified GGM/DGG $q$-series
$W_{-1}(0)$ ([physical role of $\mathrm{Im}\,q$](#conj:im-q-physical-role)). Composing,

$$
  \dim \mathcal{H}_{\mathrm{BPS}}(T[4_1])
  \;\overset{\text{GPPV}}{=}\; \Omega_{\mathrm{DT}}(4_1)
  \;\overset{\text{GGM 3(d)}}{=}\; \mathfrak{S}(4_1)
  \;=\; 3 .
$$

The value $3$ enters only from the certified Stokes computation; the bridge
class asserts no value of $A_\omega$. So the theorem *derives* that the
figure-eight observable $A_\omega$ **is** the BPS degeneracy of $T[4_1]$ and
equals $3$; it does not assume it (the non-degeneracy requirement of the bridge class).

### Scope

The result is **conditional** on the adopted bridge
[Stokes DT BPS bridge conjecture](#conj:stokes-dt-bps-bridge) **for $4_1$ as well as
in general**. Garoufalidis--Gu--Mariño state Conjecture 3(d) as a conjecture and do
not prove it for any knot. What they prove is their Conjecture 5 for $4_1$ and
$5_2$ (their Theorem 6), and they verify Conjecture 4 by computation. So no
instance of the bridge is discharged. The result is **not** carried downstream:
no mass prediction and no rung of the $Q_\beta$ ladder depends on it. The *internal*
deriving the integer $3$ directly from internal Hecke $H_3$, Bring-surface, and Wedderburn invariants (rather than importing it from Garoufalidis–Gu–Mariño) is conjectural.

The bridge here is the **closed** / state-integral BPS sector. The **open**-HOMFLY
Gukov--Stošić bridge gives the $4_1$ count $\det(4_1) = 5$ (five HOMFLY-homology
generators / five quiver nodes) and does *not* reproduce the $4_1$ Stokes integer
$3$; see the
non-degeneracy discussion in
[Stokes DT BPS bridge conjecture](#conj:stokes-dt-bps-bridge).
