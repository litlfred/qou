# Exact Attribution of the `qbeta-derived-w-overdetermined-test` Witness Move (`2026-09-03` $\to$ `2026-11-22`, Bean `qou-02g1`)

**Date:** 2026-11-24
**Bean:** `qou-02g1` (*"GAP: explain the derived-w witness move between 2026-09-05 and 2026-11-22"*)
**Target witness:** `computations/qbeta/qbeta-derived-w-overdetermined-test.witness.json` (producer: `computations/qbeta/qbeta_derived_w_overdetermined_test_probe.py`)
**Verification probe & 80-dps witness:** `computations/probes/qbeta_derived_w_witness_bisect_probe.py` $\to$ `computations/probes/qbeta-derived-w-witness-bisect.witness.json` (`compute_dps = 95`, `output_dps = 80`, `allPassed = true`)

---

## 1. Executive Verdict

**100% of the witness movement** between blob `3bd2b6d93a1` (pre-`#9055`) and blob `82c9cbc1344` (`PR #9055`, commit `8f2fdf45723`) is caused by **a single upstream change**: the **2026-09-05 intra-nucleon word-ordering fix (`intra_order="grouped"` $\to$ `"borromean"`, commits `7db032fb48` / `deb9ff5728`, bean `qou-hu1f`)** inside `pyhecke.atom.nucleon_word_letters` (called by `mass_at_3A_proper.atom_braid_word_3A`).

- **Why the chronology looked paradoxical:** Commit `8f2fdf45723` described blob `3bd2b6d93a1` as *"computed 2026-09-05 (restamped 2026-11-21)"*, making post-2026-09-05 commits appear to be the only candidates. Inspecting `git show 3bd2b6d93a1` reveals `"computedAt": "2026-09-03T04:00:37.050248+00:00"` (`commitSha: 73efaf38f59f303101bd3f94f27ae47af3a3d4f0`) — **two days BEFORE** the 2026-09-05 `grouped` $\to$ `borromean` switch!
- **All three post-2026-09-05 candidate causes named in `qou-02g1` contribute identically zero ($0.0$) to the value shift:**
  1. **`PR #8940` (`2eb8631f1ca`, exact Case C in `tr_m_word_lq`):** Contributes **$0.0$** to every trace value; it solely removed the `RuntimeError: Case C (multiple top-1 in segment) not implemented` guard that previously blocked segments like `[1, 0, 0, 1]` at $n = 3$ and interface-suffixed words at $n = 9, 12$.
  2. **`4603bfab4aa` (`per_generator_V_hat_3A` switched to `jones_wenzl`):** Contributes **$0.0$**; `qbeta_derived_w_overdetermined_test_probe.py` imports only `atom_braid_word_3A` from `mass_at_3A_proper.py` and never calls `per_generator_V_hat_3A` or `binding_3A_tower`, while `tr_m_atomic_mpfr` was already evaluating the Temperley--Lieb / $\mathrm{SU}(2)$ Markov parameter $z = q^3/(q^2+1)$ in both runs.
  3. **`89c454294aa` (seminormal disk-cache keying in `mass_at_3A_proper.py`):** Contributes **$0.0$**; the probe evaluates traces via `tr_m_atomic_mpfr` / `tr_m_atomic_mpfr_suffixes` rather than the seminormal disk cache.

---

## 2. Exact 80-dps Reproduction of Both Witnesses

Evaluating the exact $H_{3A}(q_0)$ two-row Young--Hoefsmit trace (and its closed-form $H_3(q_0)$ connected-sum factorisation) at the probe's exact $q_0 = 1.1099785827513808075916690956107688798744991218736$ reproduces **every printed digit** of both witnesses solely by toggling `intra_order="grouped"` vs `intra_order="borromean"`:

| Quantity | `3bd2b6d93a1` (`2026-09-03` witness) | Exact `intra_order="grouped"` (80 dps, truncated) | `82c9cbc1344` (`2026-11-22` witness) | Exact `intra_order="borromean"` (80 dps, truncated) |
|---|---:|---:|---:|---:|
| ${}^2\mathrm{H}$ `dtr_pred` | `0.55654466040444` | `0.556544660404438212` | `0.14704667798041` | `0.147046677980408469` |
| ${}^3\mathrm{H}$ `dtr_pred` | `0.88853612687367` | `0.888536126873670070` | `0.11292801443633` | `0.112928014436332732` |
| ${}^3\mathrm{He}$ `dtr_pred` | `0.89290857539352` | `0.892908575393515847` | `0.12958238934505` | `0.129582389345052399` |
| ${}^4\mathrm{He}$ `dtr_pred` | *(over cap)* | `1.11980900608623903` | `0.078172562842163` | `0.078172562842163179` |
| $\mathrm{tr}_M(\Delta\cdot\sigma_1)/\mathrm{tr}_M(\Delta)$ | `1.318452615852908` | `1.318452615852907714` | `0.8547993293843977` | `0.854799329384397747` |
| $\mathrm{tr}_M(\Delta\cdot L_2)/\mathrm{tr}_M(\Delta)$ | `1.275636097818101` | `1.275636097818101148` | `1.178704603211414` | `1.178704603211414303` |
| ${}^2\mathrm{H}$ $\mathrm{tr}_M(\Delta\cdot\sigma_{\mathrm{int}})/\mathrm{tr}_M(\Delta)$ | **`-0.9179091747058017`** | **`-0.917909174705801675`** | **`-0.9179091747058017`** | **`-0.917909174705801675`** |

---

## 3. Closed-Form Algebraic Mechanism of All Three Signatures

On the linear chain built by `atom_braid_word_3A(Z, N)` ($Z$ proton blocks $W_p$ on strands $\{3k, 3k+1, 3k+2\}$ followed by $N$ neutron blocks $W_n$, joined by single-letter bridges $\sigma_{3k+2} + d_k\mathbf{1}$), connected-sum multiplicativity of the Markov trace at loop weight $z = q^3/(q^2+1)$ yields exact closed-form factorisations explaining all three behaviours:

1. **Per-isotope scaling of `dtr_pred` ($3.784817\times$, $7.868164\times$, $6.890665\times$, $14.324834\times$):**
   $$\Delta\mathrm{tr}(Z, N) = \mathrm{tr}_M(W_{\mathrm{free}}) - \mathrm{tr}_M(W_{\mathrm{atom}}) = \tau_p^Z \tau_n^N \left(1 - \prod_{k=1}^{A-1}(z + d_k)\right),$$
   where the single-nucleon $H_3(q_0)$ traces of the 11-letter intra-nucleon words are:
   - `grouped` ($\sigma_0^3 \sigma_1^{-3}$ core): $\tau_p^{\mathrm{grp}} = 1.145759692457300869689\dots$, $\tau_n^{\mathrm{grp}} = 0.987743688115809571634\dots$;
   - `borromean` ($(\sigma_0\sigma_1^{-1})^3$ core): $\tau_p^{\mathrm{bor}} = 0.629328402202921918165\dots$, $\tau_n^{\mathrm{bor}} = 0.475133517155682212506\dots$.

   Because the bond factor $1 - \prod_{k=1}^{A-1}(z + d_k)$ is untouched by internal block reordering, `dtr_pred` divides by $(\tau_p^{\mathrm{grp}}/\tau_p^{\mathrm{bor}})^Z (\tau_n^{\mathrm{grp}}/\tau_n^{\mathrm{bor}})^N = (1.8206070586\dots)^Z (2.0788760542\dots)^N$, matching $3.7848166894\dots$ (${}^2\mathrm{H}$), $7.8681639512\dots$ (${}^3\mathrm{H}$), and $6.8906645169\dots$ (${}^3\mathrm{He}$) identically.

2. **Atom-independent shift of $\mathrm{tr}_M(\Delta\cdot w)/\mathrm{tr}_M(\Delta)$ for first-nucleon operators ($w \in \{\sigma_1, L_2, P_+, P_-\}$):**
   Every nucleus with $Z \ge 1$ places a proton block $W_p$ on strands $\{0,1,2\}$. Right-multiplying both $W_{\mathrm{free}}$ and $W_{\mathrm{atom}}$ by $w \in H_3(q_0)$ supported on $\{0,1\}$ replaces one factor of $\tau_p = \mathrm{tr}_M(W_p)$ by $\mathrm{tr}_M(W_p \cdot w)$ while every downstream nucleon and interface factor cancels in the ratio:
   $$\frac{\mathrm{tr}_M(\Delta_{Z,N}\cdot w)}{\mathrm{tr}_M(\Delta_{Z,N})} = \frac{\mathrm{tr}_M(W_p \cdot w)}{\mathrm{tr}_M(W_p)}.$$
   This ratio is strictly independent of $(Z, N)$ (hence all inert candidates share the exact control spread — `0.839034` across $3$ atoms under `grouped`, `2.7276` across $4$ atoms under `borromean`), yet moves from `1.318452615852908` to `0.8547993293843977` at $w = \sigma_1$ because $W_p$ itself changed from `grouped` to `borromean`.

3. **Exact 80-digit invariance of the interface-product ratio (`-0.9179091747058017` at ${}^2\mathrm{H}$ in BOTH witnesses):**
   Right-multiplying by the interface product $\prod_{k=1}^{A-1} \sigma_{3k-1}$ sends each free bridge $1 \mapsto \sigma_{3k-1}$ (trace factor $z$) and each bound bridge $(\sigma_{3k-1} + d_k\mathbf{1}) \mapsto \sigma_{3k-1}^2 + d_k\sigma_{3k-1} = (h + d_k)\sigma_{3k-1} + \mathbf{1}$ (trace factor $(h + d_k)z + 1$):
   $$\frac{\mathrm{tr}_M\bigl(\Delta_{Z,N}\cdot \prod_k \sigma_{3k-1}\bigr)}{\mathrm{tr}_M(\Delta_{Z,N})} = \frac{z^{A-1} - \prod_{k=1}^{A-1}\bigl((h + d_k)z + 1\bigr)}{1 - \prod_{k=1}^{A-1}(z + d_k)}.$$
   Here $\tau_p^Z \tau_n^N$ cancels identically! The resulting `2H` ratio `-0.917909174705801675...` agrees to all 16 printed digits between the `2026-09-03` witness and the `2026-11-22` witness — providing an independent algebraic proof that neither $z = q^3/(q^2+1)$ nor $d_{pn}$ changed between the two runs.

---

## 4. Impact on Downstream Claims

- **Qualitative anti-fit verdict unchanged:** Under both orderings, **zero** candidates in the pre-registered non-central set achieve spread $< 5\%$ (`smallest_spread = 2.60388` on `interface product` across ${}^2\mathrm{H}, {}^3\mathrm{H}, {}^3\mathrm{He}, {}^4\mathrm{He}$).
- **Why `qbeta_derived_w_overdetermined_test_probe.py` is left byte-stable here:** Its committed witness (`82c9cbc1344`, 542 s cold Rust MPFR run) is already current on `origin/main` and matches the 80-dps closed-form `borromean` values above to every printed digit; modifying `qbeta_derived_w_overdetermined_test_probe.py` for a comment-only edit would invalidate `scriptHash: 982184451911`. Instead, `computations/probes/qbeta_derived_w_witness_bisect_probe.py` certifies the full 80-dps reproduction of both witnesses in $< 20\;\mathrm{ms}$.
