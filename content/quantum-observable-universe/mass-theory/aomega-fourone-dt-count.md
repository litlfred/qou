**Theorem (conditional on [`conj:stokes-dt-bps-bridge`](#conj:stokes-dt-bps-bridge)).**
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
$W_{-1}(0)$ in [`QOU.QBeta.StokesQZeroDTCount`](#conj:im-q-physical-role). Composing,

$$
  \dim \mathcal{H}_{\mathrm{BPS}}(T[4_1])
  \;\overset{\text{GPPV}}{=}\; \Omega_{\mathrm{DT}}(4_1)
  \;\overset{\text{GGM 3(d)}}{=}\; \mathfrak{S}(4_1)
  \;=\; 3 .
$$

The value $3$ enters only from the certified Stokes computation; the bridge
class asserts no value of $A_\omega$. So the theorem *derives* that the
figure-eight observable $A_\omega$ **is** the BPS degeneracy of $T[4_1]$ and
equals $3$ — it does not assume it (the non-degeneracy requirement of the bridge class).

### Scope

This is a **theorem for $4_1$** — Garoufalidis--Gu--Mariño proved peacock
Conjecture 3 for the figure-eight, so the bridge instance is discharged there;
the *general* statement (all hyperbolic knots) is the open conjecture
[`conj:stokes-dt-bps-bridge`](#conj:stokes-dt-bps-bridge). The result is
**conditional** on that adopted bridge and is **not** carried downstream:
no mass prediction and no rung of the $Q_\beta$ ladder depends on it. The *internal*
derivation of the integer $3$ from the QOU categorical drivers (Hecke $H_3$ /
Bring / Wedderburn), rather than importing it from Garoufalidis--Gu--Mariño,
remains open.

The bridge here is the **closed** / state-integral BPS sector. The **open**-HOMFLY
Gukov--Stošić bridge gives the $4_1$ count $\det(4_1) = 5$ (five HOMFLY-homology
generators / five quiver nodes) and does *not* reproduce $\{3, 4\}$ — see the
non-degeneracy discussion in
[`conj:stokes-dt-bps-bridge`](#conj:stokes-dt-bps-bridge).
