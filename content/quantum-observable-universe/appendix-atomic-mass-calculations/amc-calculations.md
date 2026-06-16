This appendix presents the complete atomic mass calculation for all 118 elements
using the QOU Skein-lattice mass formula. For each element, we compute the
predicted mass $M_q$ from rounded CODATA constants ($\mathfrak{m}_{\mathfrak{p}} \approx :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json}$ MeV,
$\mathfrak{m}_{\mathfrak{n}} \approx :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json}$ MeV, $\mathfrak{m}_e \approx 0.511$ MeV) and compare
against $M_o$ computed from full-precision CODATA 2022 values ($\mathfrak{m}_{\mathfrak{p}} = 938.27208943$ MeV,
$\mathfrak{m}_{\mathfrak{n}} = 939.56542194$ MeV, $\mathfrak{m}_e = :val[m_e_MeV]{precision=6, witness=computations/codata-masses.witness.json}$ MeV).
Both computations use identical binding energy per nucleon $B/A$ from AME2020.
The deviation $\Delta = M_q - M_o$ therefore isolates the rounding artifact.

## Natural Elements ($Z = 1$--$92$)

### 1. Hydrogen (${}^{1}\mathrm{H}$, $Z=1$, $N=0$)

**Knot formula.** $1\mathfrak{p} \oplus 0\mathfrak{n} \oplus 1 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 1 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 0 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 938.3 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 938.3 + 1 \times 0.511 = 938.8 \text{MeV}$

**Step 3.** Binding energy: $B(1,0) = 1 \times 0.0000 = 0.0 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 938.8 - 0.0 = 938.8 \text{MeV}$

**Step 5.** Comparison: $M_o = 938.8 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.0 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 2. Helium (${}^{4}\mathrm{He}$, $Z=2$, $N=2$)

**Knot formula.** $2\mathfrak{p} \oplus 2\mathfrak{n} \oplus 2 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 2 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 2 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 3755.7 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 3755.7 + 2 \times 0.511 = 3756.7 \text{MeV}$

**Step 3.** Binding energy: $B(2,2) = 4 \times 7.0739 = 28.3 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 3756.7 - 28.3 = 3728.4 \text{MeV}$

**Step 5.** Comparison: $M_o = 3728.4 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.0 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 3. Lithium (${}^{7}\mathrm{Li}$, $Z=3$, $N=4$)

**Knot formula.** $3\mathfrak{p} \oplus 4\mathfrak{n} \oplus 3 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 3 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 4 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 6573.1 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 6573.1 + 3 \times 0.511 = 6574.6 \text{MeV}$

**Step 3.** Binding energy: $B(3,4) = 7 \times 5.6063 = 39.2 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 6574.6 - 39.2 = 6535.4 \text{MeV}$

**Step 5.** Comparison: $M_o = 6535.4 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.0 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 4. Beryllium (${}^{9}\mathrm{Be}$, $Z=4$, $N=5$)

**Knot formula.** $4\mathfrak{p} \oplus 5\mathfrak{n} \oplus 4 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 4 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 5 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 8450.9 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 8450.9 + 4 \times 0.511 = 8453.0 \text{MeV}$

**Step 3.** Binding energy: $B(4,5) = 9 \times 6.4628 = 58.2 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 8453.0 - 58.2 = 8394.8 \text{MeV}$

**Step 5.** Comparison: $M_o = 8394.8 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.0 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 5. Boron (${}^{11}\mathrm{B}$, $Z=5$, $N=6$)

**Knot formula.** $5\mathfrak{p} \oplus 6\mathfrak{n} \oplus 5 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 5 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 6 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 10328.8 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 10328.8 + 5 \times 0.511 = 10331.3 \text{MeV}$

**Step 3.** Binding energy: $B(5,6) = 11 \times 6.9277 = 76.2 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 10331.3 - 76.2 = 10255.1 \text{MeV}$

**Step 5.** Comparison: $M_o = 10255.1 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.0 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 6. Carbon (${}^{12}\mathrm{C}$, $Z=6$, $N=6$)

**Knot formula.** $6\mathfrak{p} \oplus 6\mathfrak{n} \oplus 6 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 6 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 6 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 11267.0 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 11267.0 + 6 \times 0.511 = 11270.1 \text{MeV}$

**Step 3.** Binding energy: $B(6,6) = 12 \times 7.6801 = 92.2 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 11270.1 - 92.2 = 11177.9 \text{MeV}$

**Step 5.** Comparison: $M_o = 11177.9 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.0 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 7. Nitrogen (${}^{14}\mathrm{N}$, $Z=7$, $N=7$)

**Knot formula.** $7\mathfrak{p} \oplus 7\mathfrak{n} \oplus 7 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 7 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 7 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 13144.9 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 13144.9 + 7 \times 0.511 = 13148.4 \text{MeV}$

**Step 3.** Binding energy: $B(7,7) = 14 \times 7.4756 = 104.7 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 13148.4 - 104.7 = 13043.8 \text{MeV}$

**Step 5.** Comparison: $M_o = 13043.8 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.0 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 8. Oxygen (${}^{16}\mathrm{O}$, $Z=8$, $N=8$)

**Knot formula.** $8\mathfrak{p} \oplus 8\mathfrak{n} \oplus 8 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 8 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 8 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 15022.7 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 15022.7 + 8 \times 0.511 = 15026.8 \text{MeV}$

**Step 3.** Binding energy: $B(8,8) = 16 \times 7.9762 = 127.6 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 15026.8 - 127.6 = 14899.2 \text{MeV}$

**Step 5.** Comparison: $M_o = 14899.2 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.0 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 9. Fluorine (${}^{19}\mathrm{F}$, $Z=9$, $N=10$)

**Knot formula.** $9\mathfrak{p} \oplus 10\mathfrak{n} \oplus 9 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 9 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 10 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 17840.1 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 17840.1 + 9 \times 0.511 = 17844.7 \text{MeV}$

**Step 3.** Binding energy: $B(9,10) = 19 \times 7.7790 = 147.8 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 17844.7 - 147.8 = 17696.9 \text{MeV}$

**Step 5.** Comparison: $M_o = 17696.9 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.0 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 10. Neon (${}^{20}\mathrm{Ne}$, $Z=10$, $N=10$)

**Knot formula.** $10\mathfrak{p} \oplus 10\mathfrak{n} \oplus 10 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 10 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 10 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 18778.4 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 18778.4 + 10 \times 0.511 = 18783.5 \text{MeV}$

**Step 3.** Binding energy: $B(10,10) = 20 \times 8.0325 = 160.7 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 18783.5 - 160.7 = 18622.8 \text{MeV}$

**Step 5.** Comparison: $M_o = 18622.8 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.0 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 11. Sodium (${}^{23}\mathrm{Na}$, $Z=11$, $N=12$)

**Knot formula.** $11\mathfrak{p} \oplus 12\mathfrak{n} \oplus 11 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 11 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 12 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 21595.8 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 21595.8 + 11 \times 0.511 = 21601.4 \text{MeV}$

**Step 3.** Binding energy: $B(11,12) = 23 \times 8.1115 = 186.6 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 21601.4 - 186.6 = 21414.8 \text{MeV}$

**Step 5.** Comparison: $M_o = 21414.8 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.0 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 12. Magnesium (${}^{24}\mathrm{Mg}$, $Z=12$, $N=12$)

**Knot formula.** $12\mathfrak{p} \oplus 12\mathfrak{n} \oplus 12 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 12 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 12 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 22534.0 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 22534.0 + 12 \times 0.511 = 22540.2 \text{MeV}$

**Step 3.** Binding energy: $B(12,12) = 24 \times 8.2607 = 198.3 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 22540.2 - 198.3 = 22341.9 \text{MeV}$

**Step 5.** Comparison: $M_o = 22341.9 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.0 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 13. Aluminium (${}^{27}\mathrm{Al}$, $Z=13$, $N=14$)

**Knot formula.** $13\mathfrak{p} \oplus 14\mathfrak{n} \oplus 13 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 13 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 14 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 25351.4 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 25351.4 + 13 \times 0.511 = 25358.1 \text{MeV}$

**Step 3.** Binding energy: $B(13,14) = 27 \times 8.3316 = 225.0 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 25358.1 - 225.0 = 25133.1 \text{MeV}$

**Step 5.** Comparison: $M_o = 25133.1 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.0 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 14. Silicon (${}^{28}\mathrm{Si}$, $Z=14$, $N=14$)

**Knot formula.** $14\mathfrak{p} \oplus 14\mathfrak{n} \oplus 14 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 14 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 14 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 26289.7 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 26289.7 + 14 \times 0.511 = 26296.9 \text{MeV}$

**Step 3.** Binding energy: $B(14,14) = 28 \times 8.4477 = 236.5 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 26296.9 - 236.5 = 26060.3 \text{MeV}$

**Step 5.** Comparison: $M_o = 26060.3 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.0 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 15. Phosphorus (${}^{31}\mathrm{P}$, $Z=15$, $N=16$)

**Knot formula.** $15\mathfrak{p} \oplus 16\mathfrak{n} \oplus 15 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 15 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 16 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 29107.1 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 29107.1 + 15 \times 0.511 = 29114.8 \text{MeV}$

**Step 3.** Binding energy: $B(15,16) = 31 \times 8.4812 = 262.9 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 29114.8 - 262.9 = 28851.9 \text{MeV}$

**Step 5.** Comparison: $M_o = 28851.9 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.0 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 16. Sulfur (${}^{32}\mathrm{S}$, $Z=16$, $N=16$)

**Knot formula.** $16\mathfrak{p} \oplus 16\mathfrak{n} \oplus 16 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 16 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 16 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 30045.4 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 30045.4 + 16 \times 0.511 = 30053.6 \text{MeV}$

**Step 3.** Binding energy: $B(16,16) = 32 \times 8.4932 = 271.8 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 30053.6 - 271.8 = 29781.8 \text{MeV}$

**Step 5.** Comparison: $M_o = 29781.8 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.0 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 17. Chlorine (${}^{35}\mathrm{Cl}$, $Z=17$, $N=18$)

**Knot formula.** $17\mathfrak{p} \oplus 18\mathfrak{n} \oplus 17 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 17 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 18 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 32862.8 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 32862.8 + 17 \times 0.511 = 32871.5 \text{MeV}$

**Step 3.** Binding energy: $B(17,18) = 35 \times 8.5203 = 298.2 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 32871.5 - 298.2 = 32573.3 \text{MeV}$

**Step 5.** Comparison: $M_o = 32573.3 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.0 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 18. Argon (${}^{40}\mathrm{Ar}$, $Z=18$, $N=22$)

**Knot formula.** $18\mathfrak{p} \oplus 22\mathfrak{n} \oplus 18 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 18 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 22 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 37559.3 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 37559.3 + 18 \times 0.511 = 37568.5 \text{MeV}$

**Step 3.** Binding energy: $B(18,22) = 40 \times 8.5954 = 343.8 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 37568.5 - 343.8 = 37224.7 \text{MeV}$

**Step 5.** Comparison: $M_o = 37224.7 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.0 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 19. Potassium (${}^{39}\mathrm{K}$, $Z=19$, $N=20$)

**Knot formula.** $19\mathfrak{p} \oplus 20\mathfrak{n} \oplus 19 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 19 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 20 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 36618.5 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 36618.5 + 19 \times 0.511 = 36628.2 \text{MeV}$

**Step 3.** Binding energy: $B(19,20) = 39 \times 8.5570 = 333.7 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 36628.2 - 333.7 = 36294.5 \text{MeV}$

**Step 5.** Comparison: $M_o = 36294.5 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.0 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 20. Calcium (${}^{40}\mathrm{Ca}$, $Z=20$, $N=20$)

**Knot formula.** $20\mathfrak{p} \oplus 20\mathfrak{n} \oplus 20 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 20 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 20 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 37556.7 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 37556.7 + 20 \times 0.511 = 37567.0 \text{MeV}$

**Step 3.** Binding energy: $B(20,20) = 40 \times 8.5513 = 342.1 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 37567.0 - 342.1 = 37224.9 \text{MeV}$

**Step 5.** Comparison: $M_o = 37224.9 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.0 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 21. Scandium (${}^{45}\mathrm{Sc}$, $Z=21$, $N=24$)

**Knot formula.** $21\mathfrak{p} \oplus 24\mathfrak{n} \oplus 21 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 21 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 24 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 42253.3 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 42253.3 + 21 \times 0.511 = 42264.0 \text{MeV}$

**Step 3.** Binding energy: $B(21,24) = 45 \times 8.6190 = 387.9 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 42264.0 - 387.9 = 41876.1 \text{MeV}$

**Step 5.** Comparison: $M_o = 41876.2 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.0 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 22. Titanium (${}^{48}\mathrm{Ti}$, $Z=22$, $N=26$)

**Knot formula.** $22\mathfrak{p} \oplus 26\mathfrak{n} \oplus 22 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 22 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 26 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 45070.7 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 45070.7 + 22 \times 0.511 = 45081.9 \text{MeV}$

**Step 3.** Binding energy: $B(22,26) = 48 \times 8.7230 = 418.7 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 45081.9 - 418.7 = 44663.2 \text{MeV}$

**Step 5.** Comparison: $M_o = 44663.2 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.0 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 23. Vanadium (${}^{51}\mathrm{V}$, $Z=23$, $N=28$)

**Knot formula.** $23\mathfrak{p} \oplus 28\mathfrak{n} \oplus 23 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 23 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 28 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 47888.1 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 47888.1 + 23 \times 0.511 = 47899.8 \text{MeV}$

**Step 3.** Binding energy: $B(23,28) = 51 \times 8.7420 = 445.8 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 47899.8 - 445.8 = 47454.0 \text{MeV}$

**Step 5.** Comparison: $M_o = 47454.0 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.0 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 24. Chromium (${}^{52}\mathrm{Cr}$, $Z=24$, $N=28$)

**Knot formula.** $24\mathfrak{p} \oplus 28\mathfrak{n} \oplus 24 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 24 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 28 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 48826.3 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 48826.3 + 24 \times 0.511 = 48838.6 \text{MeV}$

**Step 3.** Binding energy: $B(24,28) = 52 \times 8.7760 = 456.4 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 48838.6 - 456.4 = 48382.3 \text{MeV}$

**Step 5.** Comparison: $M_o = 48382.3 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.0 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 25. Manganese (${}^{55}\mathrm{Mn}$, $Z=25$, $N=30$)

**Knot formula.** $25\mathfrak{p} \oplus 30\mathfrak{n} \oplus 25 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 25 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 30 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 51643.8 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 51643.8 + 25 \times 0.511 = 51656.5 \text{MeV}$

**Step 3.** Binding energy: $B(25,30) = 55 \times 8.7649 = 482.1 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 51656.5 - 482.1 = 51174.5 \text{MeV}$

**Step 5.** Comparison: $M_o = 51174.5 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.0 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 26. Iron (${}^{56}\mathrm{Fe}$, $Z=26$, $N=30$)

**Knot formula.** $26\mathfrak{p} \oplus 30\mathfrak{n} \oplus 26 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 26 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 30 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 52582.0 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 52582.0 + 26 \times 0.511 = 52595.3 \text{MeV}$

**Step 3.** Binding energy: $B(26,30) = 56 \times 8.7903 = 492.3 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 52595.3 - 492.3 = 52103.1 \text{MeV}$

**Step 5.** Comparison: $M_o = 52103.1 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.0 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 27. Cobalt (${}^{59}\mathrm{Co}$, $Z=27$, $N=32$)

**Knot formula.** $27\mathfrak{p} \oplus 32\mathfrak{n} \oplus 27 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 27 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 32 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 55399.4 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 55399.4 + 27 \times 0.511 = 55413.2 \text{MeV}$

**Step 3.** Binding energy: $B(27,32) = 59 \times 8.7680 = 517.3 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 55413.2 - 517.3 = 54895.9 \text{MeV}$

**Step 5.** Comparison: $M_o = 54895.9 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.0 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 28. Nickel (${}^{58}\mathrm{Ni}$, $Z=28$, $N=30$)

**Knot formula.** $28\mathfrak{p} \oplus 30\mathfrak{n} \oplus 28 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 28 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 30 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 54458.6 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 54458.6 + 28 \times 0.511 = 54472.9 \text{MeV}$

**Step 3.** Binding energy: $B(28,30) = 58 \times 8.7322 = 506.5 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 54472.9 - 506.5 = 53966.4 \text{MeV}$

**Step 5.** Comparison: $M_o = 53966.4 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.0 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 29. Copper (${}^{63}\mathrm{Cu}$, $Z=29$, $N=34$)

**Knot formula.** $29\mathfrak{p} \oplus 34\mathfrak{n} \oplus 29 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 29 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 34 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 59155.1 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 59155.1 + 29 \times 0.511 = 59169.9 \text{MeV}$

**Step 3.** Binding energy: $B(29,34) = 63 \times 8.7522 = 551.4 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 59169.9 - 551.4 = 58618.5 \text{MeV}$

**Step 5.** Comparison: $M_o = 58618.5 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.0 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 30. Zinc (${}^{64}\mathrm{Zn}$, $Z=30$, $N=34$)

**Knot formula.** $30\mathfrak{p} \oplus 34\mathfrak{n} \oplus 30 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 30 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 34 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 60093.4 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 60093.4 + 30 \times 0.511 = 60108.7 \text{MeV}$

**Step 3.** Binding energy: $B(30,34) = 64 \times 8.7357 = 559.1 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 60108.7 - 559.1 = 59549.6 \text{MeV}$

**Step 5.** Comparison: $M_o = 59549.6 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.0 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 31. Gallium (${}^{69}\mathrm{Ga}$, $Z=31$, $N=38$)

**Knot formula.** $31\mathfrak{p} \oplus 38\mathfrak{n} \oplus 31 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 31 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 38 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 64789.9 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 64789.9 + 31 \times 0.511 = 64805.7 \text{MeV}$

**Step 3.** Binding energy: $B(31,38) = 69 \times 8.7246 = 602.0 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 64805.7 - 602.0 = 64203.7 \text{MeV}$

**Step 5.** Comparison: $M_o = 64203.8 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.0 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 32. Germanium (${}^{74}\mathrm{Ge}$, $Z=32$, $N=42$)

**Knot formula.** $32\mathfrak{p} \oplus 42\mathfrak{n} \oplus 32 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 32 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 42 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 69486.4 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 69486.4 + 32 \times 0.511 = 69502.8 \text{MeV}$

**Step 3.** Binding energy: $B(32,42) = 74 \times 8.7264 = 645.8 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 69502.8 - 645.8 = 68857.0 \text{MeV}$

**Step 5.** Comparison: $M_o = 68857.1 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.0 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 33. Arsenic (${}^{75}\mathrm{As}$, $Z=33$, $N=42$)

**Knot formula.** $33\mathfrak{p} \oplus 42\mathfrak{n} \oplus 33 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 33 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 42 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 70424.7 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 70424.7 + 33 \times 0.511 = 70441.6 \text{MeV}$

**Step 3.** Binding energy: $B(33,42) = 75 \times 8.7010 = 652.6 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 70441.6 - 652.6 = 69789.0 \text{MeV}$

**Step 5.** Comparison: $M_o = 69789.0 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.0 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 34. Selenium (${}^{80}\mathrm{Se}$, $Z=34$, $N=46$)

**Knot formula.** $34\mathfrak{p} \oplus 46\mathfrak{n} \oplus 34 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 34 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 46 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 75121.2 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 75121.2 + 34 \times 0.511 = 75138.6 \text{MeV}$

**Step 3.** Binding energy: $B(34,46) = 80 \times 8.7110 = 696.9 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 75138.6 - 696.9 = 74441.7 \text{MeV}$

**Step 5.** Comparison: $M_o = 74441.8 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.0 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 35. Bromine (${}^{79}\mathrm{Br}$, $Z=35$, $N=44$)

**Knot formula.** $35\mathfrak{p} \oplus 44\mathfrak{n} \oplus 35 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 35 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 44 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 74180.4 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 74180.4 + 35 \times 0.511 = 74198.3 \text{MeV}$

**Step 3.** Binding energy: $B(35,44) = 79 \times 8.6961 = 687.0 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 74198.3 - 687.0 = 73511.3 \text{MeV}$

**Step 5.** Comparison: $M_o = 73511.3 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.0 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 36. Krypton (${}^{84}\mathrm{Kr}$, $Z=36$, $N=48$)

**Knot formula.** $36\mathfrak{p} \oplus 48\mathfrak{n} \oplus 36 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 36 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 48 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 78876.9 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 78876.9 + 36 \times 0.511 = 78895.3 \text{MeV}$

**Step 3.** Binding energy: $B(36,48) = 84 \times 8.7172 = 732.2 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 78895.3 - 732.2 = 78163.1 \text{MeV}$

**Step 5.** Comparison: $M_o = 78163.1 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.0 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 37. Rubidium (${}^{85}\mathrm{Rb}$, $Z=37$, $N=48$)

**Knot formula.** $37\mathfrak{p} \oplus 48\mathfrak{n} \oplus 37 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 37 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 48 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 79815.2 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 79815.2 + 37 \times 0.511 = 79834.1 \text{MeV}$

**Step 3.** Binding energy: $B(37,48) = 85 \times 8.6974 = 739.3 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 79834.1 - 739.3 = 79094.8 \text{MeV}$

**Step 5.** Comparison: $M_o = 79094.8 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.0 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 38. Strontium (${}^{88}\mathrm{Sr}$, $Z=38$, $N=50$)

**Knot formula.** $38\mathfrak{p} \oplus 50\mathfrak{n} \oplus 38 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 38 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 50 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 82632.6 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 82632.6 + 38 \times 0.511 = 82652.0 \text{MeV}$

**Step 3.** Binding energy: $B(38,50) = 88 \times 8.7326 = 768.5 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 82652.0 - 768.5 = 81883.5 \text{MeV}$

**Step 5.** Comparison: $M_o = 81883.6 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.0 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 39. Yttrium (${}^{89}\mathrm{Y}$, $Z=39$, $N=50$)

**Knot formula.** $39\mathfrak{p} \oplus 50\mathfrak{n} \oplus 39 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 39 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 50 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 83570.9 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 83570.9 + 39 \times 0.511 = 83590.8 \text{MeV}$

**Step 3.** Binding energy: $B(39,50) = 89 \times 8.7138 = 775.5 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 83590.8 - 775.5 = 82815.3 \text{MeV}$

**Step 5.** Comparison: $M_o = 82815.3 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.0 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 40. Zirconium (${}^{90}\mathrm{Zr}$, $Z=40$, $N=50$)

**Knot formula.** $40\mathfrak{p} \oplus 50\mathfrak{n} \oplus 40 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 40 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 50 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 84509.1 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 84509.1 + 40 \times 0.511 = 84529.6 \text{MeV}$

**Step 3.** Binding energy: $B(40,50) = 90 \times 8.7098 = 783.9 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 84529.6 - 783.9 = 83745.7 \text{MeV}$

**Step 5.** Comparison: $M_o = 83745.7 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.0 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 41. Niobium (${}^{93}\mathrm{Nb}$, $Z=41$, $N=52$)

**Knot formula.** $41\mathfrak{p} \oplus 52\mathfrak{n} \oplus 41 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 41 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 52 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 87326.5 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 87326.5 + 41 \times 0.511 = 87347.5 \text{MeV}$

**Step 3.** Binding energy: $B(41,52) = 93 \times 8.6641 = 805.8 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 87347.5 - 805.8 = 86541.7 \text{MeV}$

**Step 5.** Comparison: $M_o = 86541.7 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.0 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 42. Molybdenum (${}^{98}\mathrm{Mo}$, $Z=42$, $N=56$)

**Knot formula.** $42\mathfrak{p} \oplus 56\mathfrak{n} \oplus 42 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 42 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 56 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 92023.1 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 92023.1 + 42 \times 0.511 = 92044.5 \text{MeV}$

**Step 3.** Binding energy: $B(42,56) = 98 \times 8.6353 = 846.3 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 92044.5 - 846.3 = 91198.3 \text{MeV}$

**Step 5.** Comparison: $M_o = 91198.3 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.0 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 43. Technetium (${}^{98}\mathrm{Tc}$, $Z=43$, $N=55$)

**Knot formula.** $43\mathfrak{p} \oplus 55\mathfrak{n} \oplus 43 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 43 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 55 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 92021.8 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 92021.8 + 43 \times 0.511 = 92043.7 \text{MeV}$

**Step 3.** Binding energy: $B(43,55) = 98 \times 8.5937 = 842.2 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 92043.7 - 842.2 = 91201.6 \text{MeV}$

**Step 5.** Comparison: $M_o = 91201.6 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.0 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 44. Ruthenium (${}^{102}\mathrm{Ru}$, $Z=44$, $N=58$)

**Knot formula.** $44\mathfrak{p} \oplus 58\mathfrak{n} \oplus 44 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 44 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 58 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 95778.7 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 95778.7 + 44 \times 0.511 = 95801.2 \text{MeV}$

**Step 3.** Binding energy: $B(44,58) = 102 \times 8.6070 = 877.9 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 95801.2 - 877.9 = 94923.3 \text{MeV}$

**Step 5.** Comparison: $M_o = 94923.3 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.0 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 45. Rhodium (${}^{103}\mathrm{Rh}$, $Z=45$, $N=58$)

**Knot formula.** $45\mathfrak{p} \oplus 58\mathfrak{n} \oplus 45 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 45 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 58 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 96717.0 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 96717.0 + 45 \times 0.511 = 96740.0 \text{MeV}$

**Step 3.** Binding energy: $B(45,58) = 103 \times 8.5843 = 884.2 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 96740.0 - 884.2 = 95855.8 \text{MeV}$

**Step 5.** Comparison: $M_o = 95855.9 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.0 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 46. Palladium (${}^{106}\mathrm{Pd}$, $Z=46$, $N=60$)

**Knot formula.** $46\mathfrak{p} \oplus 60\mathfrak{n} \oplus 46 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 46 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 60 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 99534.4 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 99534.4 + 46 \times 0.511 = 99557.9 \text{MeV}$

**Step 3.** Binding energy: $B(46,60) = 106 \times 8.5670 = 908.1 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 99557.9 - 908.1 = 98649.8 \text{MeV}$

**Step 5.** Comparison: $M_o = 98649.8 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.0 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 47. Silver (${}^{107}\mathrm{Ag}$, $Z=47$, $N=60$)

**Knot formula.** $47\mathfrak{p} \oplus 60\mathfrak{n} \oplus 47 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 47 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 60 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 100472.7 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 100472.7 + 47 \times 0.511 = 100496.7 \text{MeV}$

**Step 3.** Binding energy: $B(47,60) = 107 \times 8.5536 = 915.2 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 100496.7 - 915.2 = 99581.5 \text{MeV}$

**Step 5.** Comparison: $M_o = 99581.5 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.0 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 48. Cadmium (${}^{114}\mathrm{Cd}$, $Z=48$, $N=66$)

**Knot formula.** $48\mathfrak{p} \oplus 66\mathfrak{n} \oplus 48 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 48 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 66 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 107048.3 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 107048.3 + 48 \times 0.511 = 107072.9 \text{MeV}$

**Step 3.** Binding energy: $B(48,66) = 114 \times 8.5398 = 973.5 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 107072.9 - 973.5 = 106099.3 \text{MeV}$

**Step 5.** Comparison: $M_o = 106099.4 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.0 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 49. Indium (${}^{115}\mathrm{In}$, $Z=49$, $N=66$)

**Knot formula.** $49\mathfrak{p} \oplus 66\mathfrak{n} \oplus 49 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 49 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 66 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 107986.6 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 107986.6 + 49 \times 0.511 = 108011.7 \text{MeV}$

**Step 3.** Binding energy: $B(49,66) = 115 \times 8.5160 = 979.3 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 108011.7 - 979.3 = 107032.3 \text{MeV}$

**Step 5.** Comparison: $M_o = 107032.3 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.0 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 50. Tin (${}^{120}\mathrm{Sn}$, $Z=50$, $N=70$)

**Knot formula.** $50\mathfrak{p} \oplus 70\mathfrak{n} \oplus 50 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 50 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 70 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 112683.2 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 112683.2 + 50 \times 0.511 = 112708.7 \text{MeV}$

**Step 3.** Binding energy: $B(50,70) = 120 \times 8.5050 = 1020.6 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 112708.7 - 1020.6 = 111688.1 \text{MeV}$

**Step 5.** Comparison: $M_o = 111688.1 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.0 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 51. Antimony (${}^{121}\mathrm{Sb}$, $Z=51$, $N=70$)

**Knot formula.** $51\mathfrak{p} \oplus 70\mathfrak{n} \oplus 51 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 51 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 70 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 113621.4 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 113621.4 + 51 \times 0.511 = 113647.5 \text{MeV}$

**Step 3.** Binding energy: $B(51,70) = 121 \times 8.4820 = 1026.3 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 113647.5 - 1026.3 = 112621.2 \text{MeV}$

**Step 5.** Comparison: $M_o = 112621.2 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.0 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 52. Tellurium (${}^{130}\mathrm{Te}$, $Z=52$, $N=78$)

**Knot formula.** $52\mathfrak{p} \oplus 78\mathfrak{n} \oplus 52 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 52 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 78 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 122076.2 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 122076.2 + 52 \times 0.511 = 122102.8 \text{MeV}$

**Step 3.** Binding energy: $B(52,78) = 130 \times 8.4390 = 1097.1 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 122102.8 - 1097.1 = 121005.7 \text{MeV}$

**Step 5.** Comparison: $M_o = 121005.8 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.0 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 53. Iodine (${}^{127}\mathrm{I}$, $Z=53$, $N=74$)

**Knot formula.** $53\mathfrak{p} \oplus 74\mathfrak{n} \oplus 53 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 53 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 74 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 119256.2 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 119256.2 + 53 \times 0.511 = 119283.3 \text{MeV}$

**Step 3.** Binding energy: $B(53,74) = 127 \times 8.4455 = 1072.6 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 119283.3 - 1072.6 = 118210.7 \text{MeV}$

**Step 5.** Comparison: $M_o = 118210.8 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.0 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 54. Xenon (${}^{132}\mathrm{Xe}$, $Z=54$, $N=78$)

**Knot formula.** $54\mathfrak{p} \oplus 78\mathfrak{n} \oplus 54 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 54 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 78 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 123952.8 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 123952.8 + 54 \times 0.511 = 123980.4 \text{MeV}$

**Step 3.** Binding energy: $B(54,78) = 132 \times 8.4275 = 1112.4 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 123980.4 - 1112.4 = 122867.9 \text{MeV}$

**Step 5.** Comparison: $M_o = 122868.0 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.0 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 55. Caesium (${}^{133}\mathrm{Cs}$, $Z=55$, $N=78$)

**Knot formula.** $55\mathfrak{p} \oplus 78\mathfrak{n} \oplus 55 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 55 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 78 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 124891.0 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 124891.0 + 55 \times 0.511 = 124919.1 \text{MeV}$

**Step 3.** Binding energy: $B(55,78) = 133 \times 8.4100 = 1118.5 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 124919.1 - 1118.5 = 123800.6 \text{MeV}$

**Step 5.** Comparison: $M_o = 123800.6 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.0 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 56. Barium (${}^{138}\mathrm{Ba}$, $Z=56$, $N=82$)

**Knot formula.** $56\mathfrak{p} \oplus 82\mathfrak{n} \oplus 56 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 56 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 82 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 129587.6 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 129587.6 + 56 \times 0.511 = 129616.2 \text{MeV}$

**Step 3.** Binding energy: $B(56,82) = 138 \times 8.3937 = 1158.3 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 129616.2 - 1158.3 = 128457.8 \text{MeV}$

**Step 5.** Comparison: $M_o = 128457.9 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.0 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 57. Lanthanum (${}^{139}\mathrm{La}$, $Z=57$, $N=82$)

**Knot formula.** $57\mathfrak{p} \oplus 82\mathfrak{n} \oplus 57 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 57 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 82 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 130525.8 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 130525.8 + 57 \times 0.511 = 130555.0 \text{MeV}$

**Step 3.** Binding energy: $B(57,82) = 139 \times 8.3780 = 1164.5 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 130555.0 - 1164.5 = 129390.4 \text{MeV}$

**Step 5.** Comparison: $M_o = 129390.5 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.0 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 58. Cerium (${}^{140}\mathrm{Ce}$, $Z=58$, $N=82$)

**Knot formula.** $58\mathfrak{p} \oplus 82\mathfrak{n} \oplus 58 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 58 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 82 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 131464.1 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 131464.1 + 58 \times 0.511 = 131493.7 \text{MeV}$

**Step 3.** Binding energy: $B(58,82) = 140 \times 8.3765 = 1172.7 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 131493.7 - 1172.7 = 130321.0 \text{MeV}$

**Step 5.** Comparison: $M_o = 130321.1 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.0 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 59. Praseodymium (${}^{141}\mathrm{Pr}$, $Z=59$, $N=82$)

**Knot formula.** $59\mathfrak{p} \oplus 82\mathfrak{n} \oplus 59 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 59 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 82 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 132402.4 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 132402.4 + 59 \times 0.511 = 132432.5 \text{MeV}$

**Step 3.** Binding energy: $B(59,82) = 141 \times 8.3540 = 1177.9 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 132432.5 - 1177.9 = 131254.6 \text{MeV}$

**Step 5.** Comparison: $M_o = 131254.7 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.0 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 60. Neodymium (${}^{142}\mathrm{Nd}$, $Z=60$, $N=82$)

**Knot formula.** $60\mathfrak{p} \oplus 82\mathfrak{n} \oplus 60 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 60 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 82 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 133340.6 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 133340.6 + 60 \times 0.511 = 133371.3 \text{MeV}$

**Step 3.** Binding energy: $B(60,82) = 142 \times 8.3460 = 1185.1 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 133371.3 - 1185.1 = 132186.2 \text{MeV}$

**Step 5.** Comparison: $M_o = 132186.2 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.0 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 61. Promethium (${}^{145}\mathrm{Pm}$, $Z=61$, $N=84$)

**Knot formula.** $61\mathfrak{p} \oplus 84\mathfrak{n} \oplus 61 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 61 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 84 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 136158.1 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 136158.1 + 61 \times 0.511 = 136189.2 \text{MeV}$

**Step 3.** Binding energy: $B(61,84) = 145 \times 8.3040 = 1204.1 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 136189.2 - 1204.1 = 134985.1 \text{MeV}$

**Step 5.** Comparison: $M_o = 134985.2 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.0 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 62. Samarium (${}^{152}\mathrm{Sm}$, $Z=62$, $N=90$)

**Knot formula.** $62\mathfrak{p} \oplus 90\mathfrak{n} \oplus 62 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 62 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 90 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 142733.7 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 142733.7 + 62 \times 0.511 = 142765.4 \text{MeV}$

**Step 3.** Binding energy: $B(62,90) = 152 \times 8.2440 = 1253.1 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 142765.4 - 1253.1 = 141512.3 \text{MeV}$

**Step 5.** Comparison: $M_o = 141512.4 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.0 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 63. Europium (${}^{153}\mathrm{Eu}$, $Z=63$, $N=90$)

**Knot formula.** $63\mathfrak{p} \oplus 90\mathfrak{n} \oplus 63 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 63 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 90 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 143672.0 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 143672.0 + 63 \times 0.511 = 143704.2 \text{MeV}$

**Step 3.** Binding energy: $B(63,90) = 153 \times 8.2290 = 1259.0 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 143704.2 - 1259.0 = 142445.1 \text{MeV}$

**Step 5.** Comparison: $M_o = 142445.2 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.0 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 64. Gadolinium (${}^{158}\mathrm{Gd}$, $Z=64$, $N=94$)

**Knot formula.** $64\mathfrak{p} \oplus 94\mathfrak{n} \oplus 64 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 64 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 94 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 148368.5 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 148368.5 + 64 \times 0.511 = 148401.2 \text{MeV}$

**Step 3.** Binding energy: $B(64,94) = 158 \times 8.2140 = 1297.8 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 148401.2 - 1297.8 = 147103.4 \text{MeV}$

**Step 5.** Comparison: $M_o = 147103.5 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.0 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 65. Terbium (${}^{159}\mathrm{Tb}$, $Z=65$, $N=94$)

**Knot formula.** $65\mathfrak{p} \oplus 94\mathfrak{n} \oplus 65 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 65 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 94 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 149306.8 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 149306.8 + 65 \times 0.511 = 149340.0 \text{MeV}$

**Step 3.** Binding energy: $B(65,94) = 159 \times 8.1990 = 1303.6 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 149340.0 - 1303.6 = 148036.4 \text{MeV}$

**Step 5.** Comparison: $M_o = 148036.4 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.0 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 66. Dysprosium (${}^{164}\mathrm{Dy}$, $Z=66$, $N=98$)

**Knot formula.** $66\mathfrak{p} \oplus 98\mathfrak{n} \oplus 66 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 66 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 98 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 154003.3 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 154003.3 + 66 \times 0.511 = 154037.0 \text{MeV}$

**Step 3.** Binding energy: $B(66,98) = 164 \times 8.1865 = 1342.6 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 154037.0 - 1342.6 = 152694.5 \text{MeV}$

**Step 5.** Comparison: $M_o = 152694.5 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.0 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 67. Holmium (${}^{165}\mathrm{Ho}$, $Z=67$, $N=98$)

**Knot formula.** $67\mathfrak{p} \oplus 98\mathfrak{n} \oplus 67 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 67 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 98 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 154941.6 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 154941.6 + 67 \times 0.511 = 154975.8 \text{MeV}$

**Step 3.** Binding energy: $B(67,98) = 165 \times 8.1710 = 1348.2 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 154975.8 - 1348.2 = 153627.6 \text{MeV}$

**Step 5.** Comparison: $M_o = 153627.7 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.0 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 68. Erbium (${}^{166}\mathrm{Er}$, $Z=68$, $N=98$)

**Knot formula.** $68\mathfrak{p} \oplus 98\mathfrak{n} \oplus 68 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 68 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 98 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 155879.9 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 155879.9 + 68 \times 0.511 = 155914.6 \text{MeV}$

**Step 3.** Binding energy: $B(68,98) = 166 \times 8.1690 = 1356.1 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 155914.6 - 1356.1 = 154558.6 \text{MeV}$

**Step 5.** Comparison: $M_o = 154558.6 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.0 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 69. Thulium (${}^{169}\mathrm{Tm}$, $Z=69$, $N=100$)

**Knot formula.** $69\mathfrak{p} \oplus 100\mathfrak{n} \oplus 69 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 69 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 100 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 158697.3 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 158697.3 + 69 \times 0.511 = 158732.5 \text{MeV}$

**Step 3.** Binding energy: $B(69,100) = 169 \times 8.1460 = 1376.7 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 158732.5 - 1376.7 = 157355.9 \text{MeV}$

**Step 5.** Comparison: $M_o = 157355.9 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.0 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 70. Ytterbium (${}^{174}\mathrm{Yb}$, $Z=70$, $N=104$)

**Knot formula.** $70\mathfrak{p} \oplus 104\mathfrak{n} \oplus 70 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 70 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 104 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 163393.8 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 163393.8 + 70 \times 0.511 = 163429.6 \text{MeV}$

**Step 3.** Binding energy: $B(70,104) = 174 \times 8.1280 = 1414.3 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 163429.6 - 1414.3 = 162015.3 \text{MeV}$

**Step 5.** Comparison: $M_o = 162015.3 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.1 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 71. Lutetium (${}^{175}\mathrm{Lu}$, $Z=71$, $N=104$)

**Knot formula.** $71\mathfrak{p} \oplus 104\mathfrak{n} \oplus 71 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 71 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 104 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 164332.1 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 164332.1 + 71 \times 0.511 = 164368.4 \text{MeV}$

**Step 3.** Binding energy: $B(71,104) = 175 \times 8.1165 = 1420.4 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 164368.4 - 1420.4 = 162948.0 \text{MeV}$

**Step 5.** Comparison: $M_o = 162948.0 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.1 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 72. Hafnium (${}^{180}\mathrm{Hf}$, $Z=72$, $N=108$)

**Knot formula.** $72\mathfrak{p} \oplus 108\mathfrak{n} \oplus 72 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 72 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 108 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 169028.6 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 169028.6 + 72 \times 0.511 = 169065.4 \text{MeV}$

**Step 3.** Binding energy: $B(72,108) = 180 \times 8.0985 = 1457.7 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 169065.4 - 1457.7 = 167607.7 \text{MeV}$

**Step 5.** Comparison: $M_o = 167607.7 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.1 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 73. Tantalum (${}^{181}\mathrm{Ta}$, $Z=73$, $N=108$)

**Knot formula.** $73\mathfrak{p} \oplus 108\mathfrak{n} \oplus 73 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 73 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 108 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 169966.9 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 169966.9 + 73 \times 0.511 = 170004.2 \text{MeV}$

**Step 3.** Binding energy: $B(73,108) = 181 \times 8.0870 = 1463.7 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 170004.2 - 1463.7 = 168540.4 \text{MeV}$

**Step 5.** Comparison: $M_o = 168540.5 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.1 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 74. Tungsten (${}^{184}\mathrm{W}$, $Z=74$, $N=110$)

**Knot formula.** $74\mathfrak{p} \oplus 110\mathfrak{n} \oplus 74 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 74 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 110 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 172784.3 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 172784.3 + 74 \times 0.511 = 172822.1 \text{MeV}$

**Step 3.** Binding energy: $B(74,110) = 184 \times 8.0639 = 1483.8 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 172822.1 - 1483.8 = 171338.3 \text{MeV}$

**Step 5.** Comparison: $M_o = 171338.4 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.1 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 75. Rhenium (${}^{187}\mathrm{Re}$, $Z=75$, $N=112$)

**Knot formula.** $75\mathfrak{p} \oplus 112\mathfrak{n} \oplus 75 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 75 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 112 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 175601.7 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 175601.7 + 75 \times 0.511 = 175640.0 \text{MeV}$

**Step 3.** Binding energy: $B(75,112) = 187 \times 8.0390 = 1503.3 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 175640.0 - 1503.3 = 174136.7 \text{MeV}$

**Step 5.** Comparison: $M_o = 174136.8 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.1 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 76. Osmium (${}^{192}\mathrm{Os}$, $Z=76$, $N=116$)

**Knot formula.** $76\mathfrak{p} \oplus 116\mathfrak{n} \oplus 76 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 76 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 116 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 180298.2 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 180298.2 + 76 \times 0.511 = 180337.0 \text{MeV}$

**Step 3.** Binding energy: $B(76,116) = 192 \times 8.0194 = 1539.7 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 180337.0 - 1539.7 = 178797.3 \text{MeV}$

**Step 5.** Comparison: $M_o = 178797.4 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.1 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 77. Iridium (${}^{193}\mathrm{Ir}$, $Z=77$, $N=116$)

**Knot formula.** $77\mathfrak{p} \oplus 116\mathfrak{n} \oplus 77 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 77 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 116 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 181236.5 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 181236.5 + 77 \times 0.511 = 181275.8 \text{MeV}$

**Step 3.** Binding energy: $B(77,116) = 193 \times 8.0060 = 1545.2 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 181275.8 - 1545.2 = 179730.7 \text{MeV}$

**Step 5.** Comparison: $M_o = 179730.7 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.1 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 78. Platinum (${}^{195}\mathrm{Pt}$, $Z=78$, $N=117$)

**Knot formula.** $78\mathfrak{p} \oplus 117\mathfrak{n} \oplus 78 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 78 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 117 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 183114.3 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 183114.3 + 78 \times 0.511 = 183154.2 \text{MeV}$

**Step 3.** Binding energy: $B(78,117) = 195 \times 7.9930 = 1558.6 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 183154.2 - 1558.6 = 181595.5 \text{MeV}$

**Step 5.** Comparison: $M_o = 181595.6 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.1 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 79. Gold (${}^{197}\mathrm{Au}$, $Z=79$, $N=118$)

**Knot formula.** $79\mathfrak{p} \oplus 118\mathfrak{n} \oplus 79 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 79 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 118 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 184992.2 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 184992.2 + 79 \times 0.511 = 185032.5 \text{MeV}$

**Step 3.** Binding energy: $B(79,118) = 197 \times 7.9759 = 1571.3 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 185032.5 - 1571.3 = 183461.3 \text{MeV}$

**Step 5.** Comparison: $M_o = 183461.3 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.1 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 80. Mercury (${}^{202}\mathrm{Hg}$, $Z=80$, $N=122$)

**Knot formula.** $80\mathfrak{p} \oplus 122\mathfrak{n} \oplus 80 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 80 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 122 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 189688.7 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 189688.7 + 80 \times 0.511 = 189729.6 \text{MeV}$

**Step 3.** Binding energy: $B(80,122) = 202 \times 7.9530 = 1606.5 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 189729.6 - 1606.5 = 188123.1 \text{MeV}$

**Step 5.** Comparison: $M_o = 188123.1 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.1 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 81. Thallium (${}^{205}\mathrm{Tl}$, $Z=81$, $N=124$)

**Knot formula.** $81\mathfrak{p} \oplus 124\mathfrak{n} \oplus 81 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 81 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 124 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 192506.1 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 192506.1 + 81 \times 0.511 = 192547.5 \text{MeV}$

**Step 3.** Binding energy: $B(81,124) = 205 \times 7.9370 = 1627.1 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 192547.5 - 1627.1 = 190920.4 \text{MeV}$

**Step 5.** Comparison: $M_o = 190920.5 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.1 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 82. Lead (${}^{208}\mathrm{Pb}$, $Z=82$, $N=126$)

**Knot formula.** $82\mathfrak{p} \oplus 126\mathfrak{n} \oplus 82 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 82 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 126 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 195323.5 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 195323.5 + 82 \times 0.511 = 195365.4 \text{MeV}$

**Step 3.** Binding energy: $B(82,126) = 208 \times 7.8675 = 1636.4 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 195365.4 - 1636.4 = 193729.0 \text{MeV}$

**Step 5.** Comparison: $M_o = 193729.0 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.1 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 83. Bismuth (${}^{209}\mathrm{Bi}$, $Z=83$, $N=126$)

**Knot formula.** $83\mathfrak{p} \oplus 126\mathfrak{n} \oplus 83 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 83 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 126 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 196261.8 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 196261.8 + 83 \times 0.511 = 196304.2 \text{MeV}$

**Step 3.** Binding energy: $B(83,126) = 209 \times 7.8480 = 1640.2 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 196304.2 - 1640.2 = 194663.9 \text{MeV}$

**Step 5.** Comparison: $M_o = 194664.0 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.1 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 84. Polonium (${}^{209}\mathrm{Po}$, $Z=84$, $N=125$)

**Knot formula.** $84\mathfrak{p} \oplus 125\mathfrak{n} \oplus 84 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 84 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 125 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 196260.5 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 196260.5 + 84 \times 0.511 = 196303.4 \text{MeV}$

**Step 3.** Binding energy: $B(84,125) = 209 \times 7.8352 = 1637.6 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 196303.4 - 1637.6 = 194665.8 \text{MeV}$

**Step 5.** Comparison: $M_o = 194665.9 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.1 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 85. Astatine (${}^{210}\mathrm{At}$, $Z=85$, $N=125$)

**Knot formula.** $85\mathfrak{p} \oplus 125\mathfrak{n} \oplus 85 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 85 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 125 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 197198.7 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 197198.7 + 85 \times 0.511 = 197242.2 \text{MeV}$

**Step 3.** Binding energy: $B(85,125) = 210 \times 7.8147 = 1641.1 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 197242.2 - 1641.1 = 195601.1 \text{MeV}$

**Step 5.** Comparison: $M_o = 195601.2 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.1 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 86. Radon (${}^{222}\mathrm{Rn}$, $Z=86$, $N=136$)

**Knot formula.** $86\mathfrak{p} \oplus 136\mathfrak{n} \oplus 86 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 86 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 136 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 208472.2 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 208472.2 + 86 \times 0.511 = 208516.2 \text{MeV}$

**Step 3.** Binding energy: $B(86,136) = 222 \times 7.7227 = 1714.4 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 208516.2 - 1714.4 = 206801.7 \text{MeV}$

**Step 5.** Comparison: $M_o = 206801.8 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.1 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 87. Francium (${}^{223}\mathrm{Fr}$, $Z=87$, $N=136$)

**Knot formula.** $87\mathfrak{p} \oplus 136\mathfrak{n} \oplus 87 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 87 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 136 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 209410.5 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 209410.5 + 87 \times 0.511 = 209455.0 \text{MeV}$

**Step 3.** Binding energy: $B(87,136) = 223 \times 7.7095 = 1719.2 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 209455.0 - 1719.2 = 207735.7 \text{MeV}$

**Step 5.** Comparison: $M_o = 207735.8 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.1 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 88. Radium (${}^{226}\mathrm{Ra}$, $Z=88$, $N=138$)

**Knot formula.** $88\mathfrak{p} \oplus 138\mathfrak{n} \oplus 88 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 88 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 138 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 212227.9 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 212227.9 + 88 \times 0.511 = 212272.9 \text{MeV}$

**Step 3.** Binding energy: $B(88,138) = 226 \times 7.6620 = 1731.6 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 212272.9 - 1731.6 = 210541.3 \text{MeV}$

**Step 5.** Comparison: $M_o = 210541.3 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.1 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 89. Actinium (${}^{227}\mathrm{Ac}$, $Z=89$, $N=138$)

**Knot formula.** $89\mathfrak{p} \oplus 138\mathfrak{n} \oplus 89 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 89 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 138 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 213166.2 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 213166.2 + 89 \times 0.511 = 213211.7 \text{MeV}$

**Step 3.** Binding energy: $B(89,138) = 227 \times 7.6510 = 1736.8 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 213211.7 - 1736.8 = 211474.9 \text{MeV}$

**Step 5.** Comparison: $M_o = 211474.9 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.1 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 90. Thorium (${}^{232}\mathrm{Th}$, $Z=90$, $N=142$)

**Knot formula.** $90\mathfrak{p} \oplus 142\mathfrak{n} \oplus 90 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 90 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 142 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 217862.7 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 217862.7 + 90 \times 0.511 = 217908.7 \text{MeV}$

**Step 3.** Binding energy: $B(90,142) = 232 \times 7.6150 = 1766.7 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 217908.7 - 1766.7 = 216142.0 \text{MeV}$

**Step 5.** Comparison: $M_o = 216142.1 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.1 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 91. Protactinium (${}^{231}\mathrm{Pa}$, $Z=91$, $N=140$)

**Knot formula.** $91\mathfrak{p} \oplus 140\mathfrak{n} \oplus 91 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 91 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 140 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 216921.9 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 216921.9 + 91 \times 0.511 = 216968.4 \text{MeV}$

**Step 3.** Binding energy: $B(91,140) = 231 \times 7.6138 = 1758.8 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 216968.4 - 1758.8 = 215209.6 \text{MeV}$

**Step 5.** Comparison: $M_o = 215209.6 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.1 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 92. Uranium (${}^{238}\mathrm{U}$, $Z=92$, $N=146$)

**Knot formula.** $92\mathfrak{p} \oplus 146\mathfrak{n} \oplus 92 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 92 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 146 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 223497.5 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 223497.5 + 92 \times 0.511 = 223544.5 \text{MeV}$

**Step 3.** Binding energy: $B(92,146) = 238 \times 7.5701 = 1801.7 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 223544.5 - 1801.7 = 221742.8 \text{MeV}$

**Step 5.** Comparison: $M_o = 221742.9 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.1 \text{MeV}$ ($\delta = 0.0000\%$)

---

## Synthetic Elements ($Z = 93$--$118$)

### 93. Neptunium (${}^{237}\mathrm{Np}$, $Z=93$, $N=144$)

**Knot formula.** $93\mathfrak{p} \oplus 144\mathfrak{n} \oplus 93 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 93 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 144 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 222556.7 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 222556.7 + 93 \times 0.511 = 222604.2 \text{MeV}$

**Step 3.** Binding energy: $B(93,144) = 237 \times 7.5753 = 1795.3 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 222604.2 - 1795.3 = 220808.8 \text{MeV}$

**Step 5.** Comparison: $M_o = 220808.9 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.1 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 94. Plutonium (${}^{244}\mathrm{Pu}$, $Z=94$, $N=150$)

**Knot formula.** $94\mathfrak{p} \oplus 150\mathfrak{n} \oplus 94 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 94 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 150 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 229132.3 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 229132.3 + 94 \times 0.511 = 229180.4 \text{MeV}$

**Step 3.** Binding energy: $B(94,150) = 244 \times 7.5242 = 1835.9 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 229180.4 - 1835.9 = 227344.4 \text{MeV}$

**Step 5.** Comparison: $M_o = 227344.5 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.1 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 95. Americium (${}^{243}\mathrm{Am}$, $Z=95$, $N=148$)

**Knot formula.** $95\mathfrak{p} \oplus 148\mathfrak{n} \oplus 95 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 95 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 148 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 228191.5 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 228191.5 + 95 \times 0.511 = 228240.0 \text{MeV}$

**Step 3.** Binding energy: $B(95,148) = 243 \times 7.5249 = 1828.6 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 228240.0 - 1828.6 = 226411.5 \text{MeV}$

**Step 5.** Comparison: $M_o = 226411.5 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.1 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 96. Curium (${}^{247}\mathrm{Cm}$, $Z=96$, $N=151$)

**Knot formula.** $96\mathfrak{p} \oplus 151\mathfrak{n} \oplus 96 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 96 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 151 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 231948.4 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 231948.4 + 96 \times 0.511 = 231997.5 \text{MeV}$

**Step 3.** Binding energy: $B(96,151) = 247 \times 7.4988 = 1852.2 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 231997.5 - 1852.2 = 230145.3 \text{MeV}$

**Step 5.** Comparison: $M_o = 230145.4 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.1 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 97. Berkelium (${}^{247}\mathrm{Bk}$, $Z=97$, $N=150$)

**Knot formula.** $97\mathfrak{p} \oplus 150\mathfrak{n} \oplus 97 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 97 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 150 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 231947.1 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 231947.1 + 97 \times 0.511 = 231996.7 \text{MeV}$

**Step 3.** Binding energy: $B(97,150) = 247 \times 7.4980 = 1852.0 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 231996.7 - 1852.0 = 230144.7 \text{MeV}$

**Step 5.** Comparison: $M_o = 230144.8 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.1 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 98. Californium (${}^{251}\mathrm{Cf}$, $Z=98$, $N=153$)

**Knot formula.** $98\mathfrak{p} \oplus 153\mathfrak{n} \oplus 98 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 98 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 153 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 235704.1 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 235704.1 + 98 \times 0.511 = 235754.2 \text{MeV}$

**Step 3.** Binding energy: $B(98,153) = 251 \times 7.4688 = 1874.7 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 235754.2 - 1874.7 = 233879.5 \text{MeV}$

**Step 5.** Comparison: $M_o = 233879.6 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.1 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 99. Einsteinium (${}^{252}\mathrm{Es}$, $Z=99$, $N=153$)

**Knot formula.** $99\mathfrak{p} \oplus 153\mathfrak{n} \oplus 99 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 99 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 153 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 236642.4 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 236642.4 + 99 \times 0.511 = 236693.0 \text{MeV}$

**Step 3.** Binding energy: $B(99,153) = 252 \times 7.4496 = 1877.3 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 236693.0 - 1877.3 = 234815.7 \text{MeV}$

**Step 5.** Comparison: $M_o = 234815.7 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.1 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 100. Fermium (${}^{257}\mathrm{Fm}$, $Z=100$, $N=157$)

**Knot formula.** $100\mathfrak{p} \oplus 157\mathfrak{n} \oplus 100 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 100 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 157 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 241338.9 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 241338.9 + 100 \times 0.511 = 241390.0 \text{MeV}$

**Step 3.** Binding energy: $B(100,157) = 257 \times 7.4197 = 1906.9 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 241390.0 - 1906.9 = 239483.1 \text{MeV}$

**Step 5.** Comparison: $M_o = 239483.2 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.1 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 101. Mendelevium (${}^{258}\mathrm{Md}$, $Z=101$, $N=157$)

**Knot formula.** $101\mathfrak{p} \oplus 157\mathfrak{n} \oplus 101 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 101 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 157 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 242277.2 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 242277.2 + 101 \times 0.511 = 242328.8 \text{MeV}$

**Step 3.** Binding energy: $B(101,157) = 258 \times 7.4039 = 1910.2 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 242328.8 - 1910.2 = 240418.6 \text{MeV}$

**Step 5.** Comparison: $M_o = 240418.7 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.1 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 102. Nobelium (${}^{259}\mathrm{No}$, $Z=102$, $N=157$)

**Knot formula.** $102\mathfrak{p} \oplus 157\mathfrak{n} \oplus 102 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 102 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 157 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 243215.4 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 243215.4 + 102 \times 0.511 = 243267.6 \text{MeV}$

**Step 3.** Binding energy: $B(102,157) = 259 \times 7.3900 = 1914.0 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 243267.6 - 1914.0 = 241353.6 \text{MeV}$

**Step 5.** Comparison: $M_o = 241353.6 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.1 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 103. Lawrencium (${}^{266}\mathrm{Lr}$, $Z=103$, $N=163$)

**Knot formula.** $103\mathfrak{p} \oplus 163\mathfrak{n} \oplus 103 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 103 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 163 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 249791.1 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 249791.1 + 103 \times 0.511 = 249843.7 \text{MeV}$

**Step 3.** Binding energy: $B(103,163) = 266 \times 7.3540 = 1956.2 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 249843.7 - 1956.2 = 247887.6 \text{MeV}$

**Step 5.** Comparison: $M_o = 247887.7 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.1 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 104. Rutherfordium (${}^{267}\mathrm{Rf}$, $Z=104$, $N=163$)

**Knot formula.** $104\mathfrak{p} \oplus 163\mathfrak{n} \oplus 104 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 104 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 163 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 250729.4 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 250729.4 + 104 \times 0.511 = 250782.5 \text{MeV}$

**Step 3.** Binding energy: $B(104,163) = 267 \times 7.3380 = 1959.2 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 250782.5 - 1959.2 = 248823.3 \text{MeV}$

**Step 5.** Comparison: $M_o = 248823.4 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.1 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 105. Dubnium (${}^{268}\mathrm{Db}$, $Z=105$, $N=163$)

**Knot formula.** $105\mathfrak{p} \oplus 163\mathfrak{n} \oplus 105 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 105 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 163 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 251667.7 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 251667.7 + 105 \times 0.511 = 251721.3 \text{MeV}$

**Step 3.** Binding energy: $B(105,163) = 268 \times 7.3200 = 1961.8 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 251721.3 - 1961.8 = 249759.6 \text{MeV}$

**Step 5.** Comparison: $M_o = 249759.6 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.1 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 106. Seaborgium (${}^{269}\mathrm{Sg}$, $Z=106$, $N=163$)

**Knot formula.** $106\mathfrak{p} \oplus 163\mathfrak{n} \oplus 106 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 106 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 163 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 252605.9 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 252605.9 + 106 \times 0.511 = 252660.1 \text{MeV}$

**Step 3.** Binding energy: $B(106,163) = 269 \times 7.3020 = 1964.2 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 252660.1 - 1964.2 = 250695.9 \text{MeV}$

**Step 5.** Comparison: $M_o = 250695.9 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.1 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 107. Bohrium (${}^{270}\mathrm{Bh}$, $Z=107$, $N=163$)

**Knot formula.** $107\mathfrak{p} \oplus 163\mathfrak{n} \oplus 107 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 107 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 163 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 253544.2 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 253544.2 + 107 \times 0.511 = 253598.9 \text{MeV}$

**Step 3.** Binding energy: $B(107,163) = 270 \times 7.2830 = 1966.4 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 253598.9 - 1966.4 = 251632.5 \text{MeV}$

**Step 5.** Comparison: $M_o = 251632.5 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.1 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 108. Hassium (${}^{277}\mathrm{Hs}$, $Z=108$, $N=169$)

**Knot formula.** $108\mathfrak{p} \oplus 169\mathfrak{n} \oplus 108 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 108 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 169 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 260119.9 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 260119.9 + 108 \times 0.511 = 260175.0 \text{MeV}$

**Step 3.** Binding energy: $B(108,169) = 277 \times 7.2560 = 2009.9 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 260175.0 - 2009.9 = 258165.1 \text{MeV}$

**Step 5.** Comparison: $M_o = 258165.2 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.1 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 109. Meitnerium (${}^{278}\mathrm{Mt}$, $Z=109$, $N=169$)

**Knot formula.** $109\mathfrak{p} \oplus 169\mathfrak{n} \oplus 109 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 109 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 169 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 261058.1 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 261058.1 + 109 \times 0.511 = 261113.8 \text{MeV}$

**Step 3.** Binding energy: $B(109,169) = 278 \times 7.2370 = 2011.9 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 261113.8 - 2011.9 = 259101.9 \text{MeV}$

**Step 5.** Comparison: $M_o = 259102.0 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.1 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 110. Darmstadtium (${}^{281}\mathrm{Ds}$, $Z=110$, $N=171$)

**Knot formula.** $110\mathfrak{p} \oplus 171\mathfrak{n} \oplus 110 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 110 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 171 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 263875.5 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 263875.5 + 110 \times 0.511 = 263931.7 \text{MeV}$

**Step 3.** Binding energy: $B(110,171) = 281 \times 7.2110 = 2026.3 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 263931.7 - 2026.3 = 261905.5 \text{MeV}$

**Step 5.** Comparison: $M_o = 261905.5 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.1 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 111. Roentgenium (${}^{282}\mathrm{Rg}$, $Z=111$, $N=171$)

**Knot formula.** $111\mathfrak{p} \oplus 171\mathfrak{n} \oplus 111 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 111 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 171 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 264813.8 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 264813.8 + 111 \times 0.511 = 264870.5 \text{MeV}$

**Step 3.** Binding energy: $B(111,171) = 282 \times 7.1910 = 2027.9 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 264870.5 - 2027.9 = 262842.7 \text{MeV}$

**Step 5.** Comparison: $M_o = 262842.7 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.1 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 112. Copernicium (${}^{285}\mathrm{Cn}$, $Z=112$, $N=173$)

**Knot formula.** $112\mathfrak{p} \oplus 173\mathfrak{n} \oplus 112 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 112 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 173 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 267631.2 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 267631.2 + 112 \times 0.511 = 267688.4 \text{MeV}$

**Step 3.** Binding energy: $B(112,173) = 285 \times 7.1650 = 2042.0 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 267688.4 - 2042.0 = 265646.4 \text{MeV}$

**Step 5.** Comparison: $M_o = 265646.5 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.1 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 113. Nihonium (${}^{286}\mathrm{Nh}$, $Z=113$, $N=173$)

**Knot formula.** $113\mathfrak{p} \oplus 173\mathfrak{n} \oplus 113 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 113 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 173 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 268569.5 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 268569.5 + 113 \times 0.511 = 268627.2 \text{MeV}$

**Step 3.** Binding energy: $B(113,173) = 286 \times 7.1440 = 2043.2 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 268627.2 - 2043.2 = 266584.0 \text{MeV}$

**Step 5.** Comparison: $M_o = 266584.1 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.1 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 114. Flerovium (${}^{289}\mathrm{Fl}$, $Z=114$, $N=175$)

**Knot formula.** $114\mathfrak{p} \oplus 175\mathfrak{n} \oplus 114 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 114 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 175 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 271386.9 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 271386.9 + 114 \times 0.511 = 271445.1 \text{MeV}$

**Step 3.** Binding energy: $B(114,175) = 289 \times 7.1180 = 2057.1 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 271445.1 - 2057.1 = 269388.0 \text{MeV}$

**Step 5.** Comparison: $M_o = 269388.1 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.1 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 115. Moscovium (${}^{290}\mathrm{Mc}$, $Z=115$, $N=175$)

**Knot formula.** $115\mathfrak{p} \oplus 175\mathfrak{n} \oplus 115 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 115 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 175 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 272325.2 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 272325.2 + 115 \times 0.511 = 272383.9 \text{MeV}$

**Step 3.** Binding energy: $B(115,175) = 290 \times 7.0960 = 2057.8 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 272383.9 - 2057.8 = 270326.1 \text{MeV}$

**Step 5.** Comparison: $M_o = 270326.2 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.1 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 116. Livermorium (${}^{293}\mathrm{Lv}$, $Z=116$, $N=177$)

**Knot formula.** $116\mathfrak{p} \oplus 177\mathfrak{n} \oplus 116 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 116 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 177 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 275142.6 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 275142.6 + 116 \times 0.511 = 275201.8 \text{MeV}$

**Step 3.** Binding energy: $B(116,177) = 293 \times 7.0200 = 2056.9 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 275201.8 - 2056.9 = 273145.0 \text{MeV}$

**Step 5.** Comparison: $M_o = 273145.1 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.1 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 117. Tennessine (${}^{294}\mathrm{Ts}$, $Z=117$, $N=177$)

**Knot formula.** $117\mathfrak{p} \oplus 177\mathfrak{n} \oplus 117 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 117 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 177 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 276080.8 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 276080.8 + 117 \times 0.511 = 276140.6 \text{MeV}$

**Step 3.** Binding energy: $B(117,177) = 294 \times 6.9960 = 2056.8 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 276140.6 - 2056.8 = 274083.8 \text{MeV}$

**Step 5.** Comparison: $M_o = 274083.9 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.1 \text{MeV}$ ($\delta = 0.0000\%$)

---

### 118. Oganesson (${}^{294}\mathrm{Og}$, $Z=118$, $N=176$)

**Knot formula.** $118\mathfrak{p} \oplus 176\mathfrak{n} \oplus 118 \cdot T_{2,3}$

**Step 1.** Free nucleon mass: $M_{\text{free}} = 118 \times :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} + 176 \times :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json} = 276079.5 \text{MeV}$

**Step 2.** Add electron mass: $M_{\text{free+e}} = 276079.5 + 118 \times 0.511 = 276139.8 \text{MeV}$

**Step 3.** Binding energy: $B(118,176) = 294 \times 6.9720 = 2049.8 \text{MeV}$

**Step 4.** QOU predicted mass: $M_q = 276139.8 - 2049.8 = 274090.1 \text{MeV}$

**Step 5.** Comparison: $M_o = 274090.2 \text{MeV}$ (CODATA 2022 precise), $|\Delta| = 0.1 \text{MeV}$ ($\delta = 0.0000\%$)

---
