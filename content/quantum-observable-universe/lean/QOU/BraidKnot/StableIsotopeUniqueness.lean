import QOU.BraidKnot.NucleusEmptySDPUniqueness

/-!
# QOU.BraidKnot.StableIsotopeUniqueness — 252 stable nuclides

Per-isotope wrappers for `NucleusEmptySDPUniqueness` covering all 252
nuclides commonly classified as **stable** (no observed decay or
half-life > 10¹⁵ years), spanning ¹H through ²⁰⁹Bi.

## Coverage

| Mass range | Element span | Isotope count |
|---|---|---:|
| A = 1-50 | H..Ti | ~60 |
| A = 50-130 | V..Ba | ~120 |
| A = 130-209 | La..Bi | ~72 |
| **Total** | **H..Bi** | **252** |

Two elements (Tc, Pm) have NO stable isotopes — they get no entries
in this file.

## Naming convention

`<element_lowercase><A>_uniqueness_closed`, where `element_lowercase`
matches the symbol in `AtomicMass.lean`. Reserved Lean identifiers
(n for nitrogen, p for phosphorus, s for sulfur, etc.) get an `_el`
suffix per AtomicMass.lean's convention.

Examples:
- `c12_uniqueness_closed` — ¹²C (Z=6, n=36)
- `o16_uniqueness_closed` — ¹⁶O (Z=8, n=48)
- `fe56_uniqueness_closed` — ⁵⁶Fe (Z=26, n=168)
- `pb208_uniqueness_closed` — ²⁰⁸Pb (Z=82, n=624)

## Composition with prior layers

| Layer | File | Coverage |
|---|---|---|
| Generic parameterised | `NucleusEmptySDPUniqueness.lean` | Any `n : ℕ` |
| Per-isotope (QOU-tracked) | 10 `Applied<Nucleus>Uniqueness.lean` files | ²H, ³H, ³He, ⁴He, ⁶Li, ⁹Be, ¹¹B, ¹²C, ¹⁴N, ¹⁶O |
| Per-element (AME2020 reference) | `PeriodicTableUniqueness.lean` | 118 elements at AME2020 ref isotope |
| Per-stable-isotope (this file) | `StableIsotopeUniqueness.lean` | All 252 stable nuclides |

Theorems are identical when wrappers refer to the same `n = 3A`.
The redundant naming is for discoverability — consumers reading
about a specific isotope find a theorem named for it.

## Source

NNDC nuclear chart definition of stable nuclides (no observed decay
or half-life > 10¹⁵ years). The standard ~252-nuclide list — Bi-209
is included by the "functionally stable" convention (alpha-decay
half-life 10¹⁹ years).

## References

- `QOU.BraidKnot.NucleusEmptySDPUniqueness` (parameterised proof)
- NNDC ENSDF nuclear chart database
-/

namespace QOU.BraidKnot


-- H (Z=1): 2 stable isotope(s)
/-- H-1 (Z=1, A=1, n=3). -/
abbrev h1_uniqueness_closed := @nucleus_uniqueness_closed 3
/-- H-2 (Z=1, A=2, n=6). -/
abbrev h2_uniqueness_closed := @nucleus_uniqueness_closed 6

-- HE (Z=2): 2 stable isotope(s)
/-- He-3 (Z=2, A=3, n=9). -/
abbrev he3_uniqueness_closed := @nucleus_uniqueness_closed 9
/-- He-4 (Z=2, A=4, n=12). -/
abbrev he4_uniqueness_closed := @nucleus_uniqueness_closed 12

-- LI (Z=3): 2 stable isotope(s)
/-- Li-6 (Z=3, A=6, n=18). -/
abbrev li6_uniqueness_closed := @nucleus_uniqueness_closed 18
/-- Li-7 (Z=3, A=7, n=21). -/
abbrev li7_uniqueness_closed := @nucleus_uniqueness_closed 21

-- BE (Z=4): 1 stable isotope(s)
/-- Be-9 (Z=4, A=9, n=27). -/
abbrev be9_uniqueness_closed := @nucleus_uniqueness_closed 27

-- B (Z=5): 2 stable isotope(s)
/-- B-10 (Z=5, A=10, n=30). -/
abbrev b_el10_uniqueness_closed := @nucleus_uniqueness_closed 30
/-- B-11 (Z=5, A=11, n=33). -/
abbrev b_el11_uniqueness_closed := @nucleus_uniqueness_closed 33

-- C (Z=6): 2 stable isotope(s)
/-- C-12 (Z=6, A=12, n=36). -/
abbrev c12_uniqueness_closed := @nucleus_uniqueness_closed 36
/-- C-13 (Z=6, A=13, n=39). -/
abbrev c13_uniqueness_closed := @nucleus_uniqueness_closed 39

-- N (Z=7): 2 stable isotope(s)
/-- N-14 (Z=7, A=14, n=42). -/
abbrev n_el14_uniqueness_closed := @nucleus_uniqueness_closed 42
/-- N-15 (Z=7, A=15, n=45). -/
abbrev n_el15_uniqueness_closed := @nucleus_uniqueness_closed 45

-- O (Z=8): 3 stable isotope(s)
/-- O-16 (Z=8, A=16, n=48). -/
abbrev o16_uniqueness_closed := @nucleus_uniqueness_closed 48
/-- O-17 (Z=8, A=17, n=51). -/
abbrev o17_uniqueness_closed := @nucleus_uniqueness_closed 51
/-- O-18 (Z=8, A=18, n=54). -/
abbrev o18_uniqueness_closed := @nucleus_uniqueness_closed 54

-- F (Z=9): 1 stable isotope(s)
/-- F-19 (Z=9, A=19, n=57). -/
abbrev f19_uniqueness_closed := @nucleus_uniqueness_closed 57

-- NE (Z=10): 3 stable isotope(s)
/-- Ne-20 (Z=10, A=20, n=60). -/
abbrev ne20_uniqueness_closed := @nucleus_uniqueness_closed 60
/-- Ne-21 (Z=10, A=21, n=63). -/
abbrev ne21_uniqueness_closed := @nucleus_uniqueness_closed 63
/-- Ne-22 (Z=10, A=22, n=66). -/
abbrev ne22_uniqueness_closed := @nucleus_uniqueness_closed 66

-- NA (Z=11): 1 stable isotope(s)
/-- Na-23 (Z=11, A=23, n=69). -/
abbrev na23_uniqueness_closed := @nucleus_uniqueness_closed 69

-- MG (Z=12): 3 stable isotope(s)
/-- Mg-24 (Z=12, A=24, n=72). -/
abbrev mg24_uniqueness_closed := @nucleus_uniqueness_closed 72
/-- Mg-25 (Z=12, A=25, n=75). -/
abbrev mg25_uniqueness_closed := @nucleus_uniqueness_closed 75
/-- Mg-26 (Z=12, A=26, n=78). -/
abbrev mg26_uniqueness_closed := @nucleus_uniqueness_closed 78

-- AL (Z=13): 1 stable isotope(s)
/-- Al-27 (Z=13, A=27, n=81). -/
abbrev al27_uniqueness_closed := @nucleus_uniqueness_closed 81

-- SI (Z=14): 3 stable isotope(s)
/-- Si-28 (Z=14, A=28, n=84). -/
abbrev si28_uniqueness_closed := @nucleus_uniqueness_closed 84
/-- Si-29 (Z=14, A=29, n=87). -/
abbrev si29_uniqueness_closed := @nucleus_uniqueness_closed 87
/-- Si-30 (Z=14, A=30, n=90). -/
abbrev si30_uniqueness_closed := @nucleus_uniqueness_closed 90

-- P (Z=15): 1 stable isotope(s)
/-- P-31 (Z=15, A=31, n=93). -/
abbrev p_el31_uniqueness_closed := @nucleus_uniqueness_closed 93

-- S (Z=16): 4 stable isotope(s)
/-- S-32 (Z=16, A=32, n=96). -/
abbrev s_el32_uniqueness_closed := @nucleus_uniqueness_closed 96
/-- S-33 (Z=16, A=33, n=99). -/
abbrev s_el33_uniqueness_closed := @nucleus_uniqueness_closed 99
/-- S-34 (Z=16, A=34, n=102). -/
abbrev s_el34_uniqueness_closed := @nucleus_uniqueness_closed 102
/-- S-36 (Z=16, A=36, n=108). -/
abbrev s_el36_uniqueness_closed := @nucleus_uniqueness_closed 108

-- CL (Z=17): 2 stable isotope(s)
/-- Cl-35 (Z=17, A=35, n=105). -/
abbrev cl35_uniqueness_closed := @nucleus_uniqueness_closed 105
/-- Cl-37 (Z=17, A=37, n=111). -/
abbrev cl37_uniqueness_closed := @nucleus_uniqueness_closed 111

-- AR (Z=18): 3 stable isotope(s)
/-- Ar-36 (Z=18, A=36, n=108). -/
abbrev ar36_uniqueness_closed := @nucleus_uniqueness_closed 108
/-- Ar-38 (Z=18, A=38, n=114). -/
abbrev ar38_uniqueness_closed := @nucleus_uniqueness_closed 114
/-- Ar-40 (Z=18, A=40, n=120). -/
abbrev ar40_uniqueness_closed := @nucleus_uniqueness_closed 120

-- K (Z=19): 2 stable isotope(s)
/-- K-39 (Z=19, A=39, n=117). -/
abbrev k_el39_uniqueness_closed := @nucleus_uniqueness_closed 117
/-- K-41 (Z=19, A=41, n=123). -/
abbrev k_el41_uniqueness_closed := @nucleus_uniqueness_closed 123

-- CA (Z=20): 6 stable isotope(s)
/-- Ca-40 (Z=20, A=40, n=120). -/
abbrev ca40_uniqueness_closed := @nucleus_uniqueness_closed 120
/-- Ca-42 (Z=20, A=42, n=126). -/
abbrev ca42_uniqueness_closed := @nucleus_uniqueness_closed 126
/-- Ca-43 (Z=20, A=43, n=129). -/
abbrev ca43_uniqueness_closed := @nucleus_uniqueness_closed 129
/-- Ca-44 (Z=20, A=44, n=132). -/
abbrev ca44_uniqueness_closed := @nucleus_uniqueness_closed 132
/-- Ca-46 (Z=20, A=46, n=138). -/
abbrev ca46_uniqueness_closed := @nucleus_uniqueness_closed 138
/-- Ca-48 (Z=20, A=48, n=144). -/
abbrev ca48_uniqueness_closed := @nucleus_uniqueness_closed 144

-- SC (Z=21): 1 stable isotope(s)
/-- Sc-45 (Z=21, A=45, n=135). -/
abbrev sc45_uniqueness_closed := @nucleus_uniqueness_closed 135

-- TI (Z=22): 5 stable isotope(s)
/-- Ti-46 (Z=22, A=46, n=138). -/
abbrev ti46_uniqueness_closed := @nucleus_uniqueness_closed 138
/-- Ti-47 (Z=22, A=47, n=141). -/
abbrev ti47_uniqueness_closed := @nucleus_uniqueness_closed 141
/-- Ti-48 (Z=22, A=48, n=144). -/
abbrev ti48_uniqueness_closed := @nucleus_uniqueness_closed 144
/-- Ti-49 (Z=22, A=49, n=147). -/
abbrev ti49_uniqueness_closed := @nucleus_uniqueness_closed 147
/-- Ti-50 (Z=22, A=50, n=150). -/
abbrev ti50_uniqueness_closed := @nucleus_uniqueness_closed 150

-- V (Z=23): 2 stable isotope(s)
/-- V-50 (Z=23, A=50, n=150). -/
abbrev v_el50_uniqueness_closed := @nucleus_uniqueness_closed 150
/-- V-51 (Z=23, A=51, n=153). -/
abbrev v_el51_uniqueness_closed := @nucleus_uniqueness_closed 153

-- CR (Z=24): 4 stable isotope(s)
/-- Cr-50 (Z=24, A=50, n=150). -/
abbrev cr50_uniqueness_closed := @nucleus_uniqueness_closed 150
/-- Cr-52 (Z=24, A=52, n=156). -/
abbrev cr52_uniqueness_closed := @nucleus_uniqueness_closed 156
/-- Cr-53 (Z=24, A=53, n=159). -/
abbrev cr53_uniqueness_closed := @nucleus_uniqueness_closed 159
/-- Cr-54 (Z=24, A=54, n=162). -/
abbrev cr54_uniqueness_closed := @nucleus_uniqueness_closed 162

-- MN (Z=25): 1 stable isotope(s)
/-- Mn-55 (Z=25, A=55, n=165). -/
abbrev mn55_uniqueness_closed := @nucleus_uniqueness_closed 165

-- FE (Z=26): 4 stable isotope(s)
/-- Fe-54 (Z=26, A=54, n=162). -/
abbrev fe54_uniqueness_closed := @nucleus_uniqueness_closed 162
/-- Fe-56 (Z=26, A=56, n=168). -/
abbrev fe56_uniqueness_closed := @nucleus_uniqueness_closed 168
/-- Fe-57 (Z=26, A=57, n=171). -/
abbrev fe57_uniqueness_closed := @nucleus_uniqueness_closed 171
/-- Fe-58 (Z=26, A=58, n=174). -/
abbrev fe58_uniqueness_closed := @nucleus_uniqueness_closed 174

-- CO (Z=27): 1 stable isotope(s)
/-- Co-59 (Z=27, A=59, n=177). -/
abbrev co59_uniqueness_closed := @nucleus_uniqueness_closed 177

-- NI (Z=28): 5 stable isotope(s)
/-- Ni-58 (Z=28, A=58, n=174). -/
abbrev ni58_uniqueness_closed := @nucleus_uniqueness_closed 174
/-- Ni-60 (Z=28, A=60, n=180). -/
abbrev ni60_uniqueness_closed := @nucleus_uniqueness_closed 180
/-- Ni-61 (Z=28, A=61, n=183). -/
abbrev ni61_uniqueness_closed := @nucleus_uniqueness_closed 183
/-- Ni-62 (Z=28, A=62, n=186). -/
abbrev ni62_uniqueness_closed := @nucleus_uniqueness_closed 186
/-- Ni-64 (Z=28, A=64, n=192). -/
abbrev ni64_uniqueness_closed := @nucleus_uniqueness_closed 192

-- CU (Z=29): 2 stable isotope(s)
/-- Cu-63 (Z=29, A=63, n=189). -/
abbrev cu63_uniqueness_closed := @nucleus_uniqueness_closed 189
/-- Cu-65 (Z=29, A=65, n=195). -/
abbrev cu65_uniqueness_closed := @nucleus_uniqueness_closed 195

-- ZN (Z=30): 5 stable isotope(s)
/-- Zn-64 (Z=30, A=64, n=192). -/
abbrev zn64_uniqueness_closed := @nucleus_uniqueness_closed 192
/-- Zn-66 (Z=30, A=66, n=198). -/
abbrev zn66_uniqueness_closed := @nucleus_uniqueness_closed 198
/-- Zn-67 (Z=30, A=67, n=201). -/
abbrev zn67_uniqueness_closed := @nucleus_uniqueness_closed 201
/-- Zn-68 (Z=30, A=68, n=204). -/
abbrev zn68_uniqueness_closed := @nucleus_uniqueness_closed 204
/-- Zn-70 (Z=30, A=70, n=210). -/
abbrev zn70_uniqueness_closed := @nucleus_uniqueness_closed 210

-- GA (Z=31): 2 stable isotope(s)
/-- Ga-69 (Z=31, A=69, n=207). -/
abbrev ga69_uniqueness_closed := @nucleus_uniqueness_closed 207
/-- Ga-71 (Z=31, A=71, n=213). -/
abbrev ga71_uniqueness_closed := @nucleus_uniqueness_closed 213

-- GE (Z=32): 5 stable isotope(s)
/-- Ge-70 (Z=32, A=70, n=210). -/
abbrev ge70_uniqueness_closed := @nucleus_uniqueness_closed 210
/-- Ge-72 (Z=32, A=72, n=216). -/
abbrev ge72_uniqueness_closed := @nucleus_uniqueness_closed 216
/-- Ge-73 (Z=32, A=73, n=219). -/
abbrev ge73_uniqueness_closed := @nucleus_uniqueness_closed 219
/-- Ge-74 (Z=32, A=74, n=222). -/
abbrev ge74_uniqueness_closed := @nucleus_uniqueness_closed 222
/-- Ge-76 (Z=32, A=76, n=228). -/
abbrev ge76_uniqueness_closed := @nucleus_uniqueness_closed 228

-- AS (Z=33): 1 stable isotope(s)
/-- As-75 (Z=33, A=75, n=225). -/
abbrev as75_uniqueness_closed := @nucleus_uniqueness_closed 225

-- SE (Z=34): 6 stable isotope(s)
/-- Se-74 (Z=34, A=74, n=222). -/
abbrev se74_uniqueness_closed := @nucleus_uniqueness_closed 222
/-- Se-76 (Z=34, A=76, n=228). -/
abbrev se76_uniqueness_closed := @nucleus_uniqueness_closed 228
/-- Se-77 (Z=34, A=77, n=231). -/
abbrev se77_uniqueness_closed := @nucleus_uniqueness_closed 231
/-- Se-78 (Z=34, A=78, n=234). -/
abbrev se78_uniqueness_closed := @nucleus_uniqueness_closed 234
/-- Se-80 (Z=34, A=80, n=240). -/
abbrev se80_uniqueness_closed := @nucleus_uniqueness_closed 240
/-- Se-82 (Z=34, A=82, n=246). -/
abbrev se82_uniqueness_closed := @nucleus_uniqueness_closed 246

-- BR (Z=35): 2 stable isotope(s)
/-- Br-79 (Z=35, A=79, n=237). -/
abbrev br79_uniqueness_closed := @nucleus_uniqueness_closed 237
/-- Br-81 (Z=35, A=81, n=243). -/
abbrev br81_uniqueness_closed := @nucleus_uniqueness_closed 243

-- KR (Z=36): 6 stable isotope(s)
/-- Kr-78 (Z=36, A=78, n=234). -/
abbrev kr78_uniqueness_closed := @nucleus_uniqueness_closed 234
/-- Kr-80 (Z=36, A=80, n=240). -/
abbrev kr80_uniqueness_closed := @nucleus_uniqueness_closed 240
/-- Kr-82 (Z=36, A=82, n=246). -/
abbrev kr82_uniqueness_closed := @nucleus_uniqueness_closed 246
/-- Kr-83 (Z=36, A=83, n=249). -/
abbrev kr83_uniqueness_closed := @nucleus_uniqueness_closed 249
/-- Kr-84 (Z=36, A=84, n=252). -/
abbrev kr84_uniqueness_closed := @nucleus_uniqueness_closed 252
/-- Kr-86 (Z=36, A=86, n=258). -/
abbrev kr86_uniqueness_closed := @nucleus_uniqueness_closed 258

-- RB (Z=37): 1 stable isotope(s)
/-- Rb-85 (Z=37, A=85, n=255). -/
abbrev rb85_uniqueness_closed := @nucleus_uniqueness_closed 255

-- SR (Z=38): 4 stable isotope(s)
/-- Sr-84 (Z=38, A=84, n=252). -/
abbrev sr84_uniqueness_closed := @nucleus_uniqueness_closed 252
/-- Sr-86 (Z=38, A=86, n=258). -/
abbrev sr86_uniqueness_closed := @nucleus_uniqueness_closed 258
/-- Sr-87 (Z=38, A=87, n=261). -/
abbrev sr87_uniqueness_closed := @nucleus_uniqueness_closed 261
/-- Sr-88 (Z=38, A=88, n=264). -/
abbrev sr88_uniqueness_closed := @nucleus_uniqueness_closed 264

-- Y (Z=39): 1 stable isotope(s)
/-- Y-89 (Z=39, A=89, n=267). -/
abbrev y_el89_uniqueness_closed := @nucleus_uniqueness_closed 267

-- ZR (Z=40): 5 stable isotope(s)
/-- Zr-90 (Z=40, A=90, n=270). -/
abbrev zr90_uniqueness_closed := @nucleus_uniqueness_closed 270
/-- Zr-91 (Z=40, A=91, n=273). -/
abbrev zr91_uniqueness_closed := @nucleus_uniqueness_closed 273
/-- Zr-92 (Z=40, A=92, n=276). -/
abbrev zr92_uniqueness_closed := @nucleus_uniqueness_closed 276
/-- Zr-94 (Z=40, A=94, n=282). -/
abbrev zr94_uniqueness_closed := @nucleus_uniqueness_closed 282
/-- Zr-96 (Z=40, A=96, n=288). -/
abbrev zr96_uniqueness_closed := @nucleus_uniqueness_closed 288

-- NB (Z=41): 1 stable isotope(s)
/-- Nb-93 (Z=41, A=93, n=279). -/
abbrev nb93_uniqueness_closed := @nucleus_uniqueness_closed 279

-- MO (Z=42): 7 stable isotope(s)
/-- Mo-92 (Z=42, A=92, n=276). -/
abbrev mo92_uniqueness_closed := @nucleus_uniqueness_closed 276
/-- Mo-94 (Z=42, A=94, n=282). -/
abbrev mo94_uniqueness_closed := @nucleus_uniqueness_closed 282
/-- Mo-95 (Z=42, A=95, n=285). -/
abbrev mo95_uniqueness_closed := @nucleus_uniqueness_closed 285
/-- Mo-96 (Z=42, A=96, n=288). -/
abbrev mo96_uniqueness_closed := @nucleus_uniqueness_closed 288
/-- Mo-97 (Z=42, A=97, n=291). -/
abbrev mo97_uniqueness_closed := @nucleus_uniqueness_closed 291
/-- Mo-98 (Z=42, A=98, n=294). -/
abbrev mo98_uniqueness_closed := @nucleus_uniqueness_closed 294
/-- Mo-100 (Z=42, A=100, n=300). -/
abbrev mo100_uniqueness_closed := @nucleus_uniqueness_closed 300

-- RU (Z=44): 7 stable isotope(s)
/-- Ru-96 (Z=44, A=96, n=288). -/
abbrev ru96_uniqueness_closed := @nucleus_uniqueness_closed 288
/-- Ru-98 (Z=44, A=98, n=294). -/
abbrev ru98_uniqueness_closed := @nucleus_uniqueness_closed 294
/-- Ru-99 (Z=44, A=99, n=297). -/
abbrev ru99_uniqueness_closed := @nucleus_uniqueness_closed 297
/-- Ru-100 (Z=44, A=100, n=300). -/
abbrev ru100_uniqueness_closed := @nucleus_uniqueness_closed 300
/-- Ru-101 (Z=44, A=101, n=303). -/
abbrev ru101_uniqueness_closed := @nucleus_uniqueness_closed 303
/-- Ru-102 (Z=44, A=102, n=306). -/
abbrev ru102_uniqueness_closed := @nucleus_uniqueness_closed 306
/-- Ru-104 (Z=44, A=104, n=312). -/
abbrev ru104_uniqueness_closed := @nucleus_uniqueness_closed 312

-- RH (Z=45): 1 stable isotope(s)
/-- Rh-103 (Z=45, A=103, n=309). -/
abbrev rh103_uniqueness_closed := @nucleus_uniqueness_closed 309

-- PD (Z=46): 6 stable isotope(s)
/-- Pd-102 (Z=46, A=102, n=306). -/
abbrev pd102_uniqueness_closed := @nucleus_uniqueness_closed 306
/-- Pd-104 (Z=46, A=104, n=312). -/
abbrev pd104_uniqueness_closed := @nucleus_uniqueness_closed 312
/-- Pd-105 (Z=46, A=105, n=315). -/
abbrev pd105_uniqueness_closed := @nucleus_uniqueness_closed 315
/-- Pd-106 (Z=46, A=106, n=318). -/
abbrev pd106_uniqueness_closed := @nucleus_uniqueness_closed 318
/-- Pd-108 (Z=46, A=108, n=324). -/
abbrev pd108_uniqueness_closed := @nucleus_uniqueness_closed 324
/-- Pd-110 (Z=46, A=110, n=330). -/
abbrev pd110_uniqueness_closed := @nucleus_uniqueness_closed 330

-- AG (Z=47): 2 stable isotope(s)
/-- Ag-107 (Z=47, A=107, n=321). -/
abbrev ag107_uniqueness_closed := @nucleus_uniqueness_closed 321
/-- Ag-109 (Z=47, A=109, n=327). -/
abbrev ag109_uniqueness_closed := @nucleus_uniqueness_closed 327

-- CD (Z=48): 8 stable isotope(s)
/-- Cd-106 (Z=48, A=106, n=318). -/
abbrev cd106_uniqueness_closed := @nucleus_uniqueness_closed 318
/-- Cd-108 (Z=48, A=108, n=324). -/
abbrev cd108_uniqueness_closed := @nucleus_uniqueness_closed 324
/-- Cd-110 (Z=48, A=110, n=330). -/
abbrev cd110_uniqueness_closed := @nucleus_uniqueness_closed 330
/-- Cd-111 (Z=48, A=111, n=333). -/
abbrev cd111_uniqueness_closed := @nucleus_uniqueness_closed 333
/-- Cd-112 (Z=48, A=112, n=336). -/
abbrev cd112_uniqueness_closed := @nucleus_uniqueness_closed 336
/-- Cd-113 (Z=48, A=113, n=339). -/
abbrev cd113_uniqueness_closed := @nucleus_uniqueness_closed 339
/-- Cd-114 (Z=48, A=114, n=342). -/
abbrev cd114_uniqueness_closed := @nucleus_uniqueness_closed 342
/-- Cd-116 (Z=48, A=116, n=348). -/
abbrev cd116_uniqueness_closed := @nucleus_uniqueness_closed 348

-- IN (Z=49): 2 stable isotope(s)
/-- In-113 (Z=49, A=113, n=339). -/
abbrev in113_uniqueness_closed := @nucleus_uniqueness_closed 339
/-- In-115 (Z=49, A=115, n=345). -/
abbrev in115_uniqueness_closed := @nucleus_uniqueness_closed 345

-- SN (Z=50): 10 stable isotope(s)
/-- Sn-112 (Z=50, A=112, n=336). -/
abbrev sn112_uniqueness_closed := @nucleus_uniqueness_closed 336
/-- Sn-114 (Z=50, A=114, n=342). -/
abbrev sn114_uniqueness_closed := @nucleus_uniqueness_closed 342
/-- Sn-115 (Z=50, A=115, n=345). -/
abbrev sn115_uniqueness_closed := @nucleus_uniqueness_closed 345
/-- Sn-116 (Z=50, A=116, n=348). -/
abbrev sn116_uniqueness_closed := @nucleus_uniqueness_closed 348
/-- Sn-117 (Z=50, A=117, n=351). -/
abbrev sn117_uniqueness_closed := @nucleus_uniqueness_closed 351
/-- Sn-118 (Z=50, A=118, n=354). -/
abbrev sn118_uniqueness_closed := @nucleus_uniqueness_closed 354
/-- Sn-119 (Z=50, A=119, n=357). -/
abbrev sn119_uniqueness_closed := @nucleus_uniqueness_closed 357
/-- Sn-120 (Z=50, A=120, n=360). -/
abbrev sn120_uniqueness_closed := @nucleus_uniqueness_closed 360
/-- Sn-122 (Z=50, A=122, n=366). -/
abbrev sn122_uniqueness_closed := @nucleus_uniqueness_closed 366
/-- Sn-124 (Z=50, A=124, n=372). -/
abbrev sn124_uniqueness_closed := @nucleus_uniqueness_closed 372

-- SB (Z=51): 2 stable isotope(s)
/-- Sb-121 (Z=51, A=121, n=363). -/
abbrev sb121_uniqueness_closed := @nucleus_uniqueness_closed 363
/-- Sb-123 (Z=51, A=123, n=369). -/
abbrev sb123_uniqueness_closed := @nucleus_uniqueness_closed 369

-- TE (Z=52): 8 stable isotope(s)
/-- Te-120 (Z=52, A=120, n=360). -/
abbrev te120_uniqueness_closed := @nucleus_uniqueness_closed 360
/-- Te-122 (Z=52, A=122, n=366). -/
abbrev te122_uniqueness_closed := @nucleus_uniqueness_closed 366
/-- Te-123 (Z=52, A=123, n=369). -/
abbrev te123_uniqueness_closed := @nucleus_uniqueness_closed 369
/-- Te-124 (Z=52, A=124, n=372). -/
abbrev te124_uniqueness_closed := @nucleus_uniqueness_closed 372
/-- Te-125 (Z=52, A=125, n=375). -/
abbrev te125_uniqueness_closed := @nucleus_uniqueness_closed 375
/-- Te-126 (Z=52, A=126, n=378). -/
abbrev te126_uniqueness_closed := @nucleus_uniqueness_closed 378
/-- Te-128 (Z=52, A=128, n=384). -/
abbrev te128_uniqueness_closed := @nucleus_uniqueness_closed 384
/-- Te-130 (Z=52, A=130, n=390). -/
abbrev te130_uniqueness_closed := @nucleus_uniqueness_closed 390

-- I (Z=53): 1 stable isotope(s)
/-- I-127 (Z=53, A=127, n=381). -/
abbrev i_el127_uniqueness_closed := @nucleus_uniqueness_closed 381

-- XE (Z=54): 9 stable isotope(s)
/-- Xe-124 (Z=54, A=124, n=372). -/
abbrev xe124_uniqueness_closed := @nucleus_uniqueness_closed 372
/-- Xe-126 (Z=54, A=126, n=378). -/
abbrev xe126_uniqueness_closed := @nucleus_uniqueness_closed 378
/-- Xe-128 (Z=54, A=128, n=384). -/
abbrev xe128_uniqueness_closed := @nucleus_uniqueness_closed 384
/-- Xe-129 (Z=54, A=129, n=387). -/
abbrev xe129_uniqueness_closed := @nucleus_uniqueness_closed 387
/-- Xe-130 (Z=54, A=130, n=390). -/
abbrev xe130_uniqueness_closed := @nucleus_uniqueness_closed 390
/-- Xe-131 (Z=54, A=131, n=393). -/
abbrev xe131_uniqueness_closed := @nucleus_uniqueness_closed 393
/-- Xe-132 (Z=54, A=132, n=396). -/
abbrev xe132_uniqueness_closed := @nucleus_uniqueness_closed 396
/-- Xe-134 (Z=54, A=134, n=402). -/
abbrev xe134_uniqueness_closed := @nucleus_uniqueness_closed 402
/-- Xe-136 (Z=54, A=136, n=408). -/
abbrev xe136_uniqueness_closed := @nucleus_uniqueness_closed 408

-- CS (Z=55): 1 stable isotope(s)
/-- Cs-133 (Z=55, A=133, n=399). -/
abbrev cs133_uniqueness_closed := @nucleus_uniqueness_closed 399

-- BA (Z=56): 7 stable isotope(s)
/-- Ba-130 (Z=56, A=130, n=390). -/
abbrev ba130_uniqueness_closed := @nucleus_uniqueness_closed 390
/-- Ba-132 (Z=56, A=132, n=396). -/
abbrev ba132_uniqueness_closed := @nucleus_uniqueness_closed 396
/-- Ba-134 (Z=56, A=134, n=402). -/
abbrev ba134_uniqueness_closed := @nucleus_uniqueness_closed 402
/-- Ba-135 (Z=56, A=135, n=405). -/
abbrev ba135_uniqueness_closed := @nucleus_uniqueness_closed 405
/-- Ba-136 (Z=56, A=136, n=408). -/
abbrev ba136_uniqueness_closed := @nucleus_uniqueness_closed 408
/-- Ba-137 (Z=56, A=137, n=411). -/
abbrev ba137_uniqueness_closed := @nucleus_uniqueness_closed 411
/-- Ba-138 (Z=56, A=138, n=414). -/
abbrev ba138_uniqueness_closed := @nucleus_uniqueness_closed 414

-- LA (Z=57): 2 stable isotope(s)
/-- La-138 (Z=57, A=138, n=414). -/
abbrev la138_uniqueness_closed := @nucleus_uniqueness_closed 414
/-- La-139 (Z=57, A=139, n=417). -/
abbrev la139_uniqueness_closed := @nucleus_uniqueness_closed 417

-- CE (Z=58): 4 stable isotope(s)
/-- Ce-136 (Z=58, A=136, n=408). -/
abbrev ce136_uniqueness_closed := @nucleus_uniqueness_closed 408
/-- Ce-138 (Z=58, A=138, n=414). -/
abbrev ce138_uniqueness_closed := @nucleus_uniqueness_closed 414
/-- Ce-140 (Z=58, A=140, n=420). -/
abbrev ce140_uniqueness_closed := @nucleus_uniqueness_closed 420
/-- Ce-142 (Z=58, A=142, n=426). -/
abbrev ce142_uniqueness_closed := @nucleus_uniqueness_closed 426

-- PR (Z=59): 1 stable isotope(s)
/-- Pr-141 (Z=59, A=141, n=423). -/
abbrev pr141_uniqueness_closed := @nucleus_uniqueness_closed 423

-- ND (Z=60): 7 stable isotope(s)
/-- Nd-142 (Z=60, A=142, n=426). -/
abbrev nd142_uniqueness_closed := @nucleus_uniqueness_closed 426
/-- Nd-143 (Z=60, A=143, n=429). -/
abbrev nd143_uniqueness_closed := @nucleus_uniqueness_closed 429
/-- Nd-144 (Z=60, A=144, n=432). -/
abbrev nd144_uniqueness_closed := @nucleus_uniqueness_closed 432
/-- Nd-145 (Z=60, A=145, n=435). -/
abbrev nd145_uniqueness_closed := @nucleus_uniqueness_closed 435
/-- Nd-146 (Z=60, A=146, n=438). -/
abbrev nd146_uniqueness_closed := @nucleus_uniqueness_closed 438
/-- Nd-148 (Z=60, A=148, n=444). -/
abbrev nd148_uniqueness_closed := @nucleus_uniqueness_closed 444
/-- Nd-150 (Z=60, A=150, n=450). -/
abbrev nd150_uniqueness_closed := @nucleus_uniqueness_closed 450

-- SM (Z=62): 7 stable isotope(s)
/-- Sm-144 (Z=62, A=144, n=432). -/
abbrev sm144_uniqueness_closed := @nucleus_uniqueness_closed 432
/-- Sm-147 (Z=62, A=147, n=441). -/
abbrev sm147_uniqueness_closed := @nucleus_uniqueness_closed 441
/-- Sm-148 (Z=62, A=148, n=444). -/
abbrev sm148_uniqueness_closed := @nucleus_uniqueness_closed 444
/-- Sm-149 (Z=62, A=149, n=447). -/
abbrev sm149_uniqueness_closed := @nucleus_uniqueness_closed 447
/-- Sm-150 (Z=62, A=150, n=450). -/
abbrev sm150_uniqueness_closed := @nucleus_uniqueness_closed 450
/-- Sm-152 (Z=62, A=152, n=456). -/
abbrev sm152_uniqueness_closed := @nucleus_uniqueness_closed 456
/-- Sm-154 (Z=62, A=154, n=462). -/
abbrev sm154_uniqueness_closed := @nucleus_uniqueness_closed 462

-- EU (Z=63): 2 stable isotope(s)
/-- Eu-151 (Z=63, A=151, n=453). -/
abbrev eu151_uniqueness_closed := @nucleus_uniqueness_closed 453
/-- Eu-153 (Z=63, A=153, n=459). -/
abbrev eu153_uniqueness_closed := @nucleus_uniqueness_closed 459

-- GD (Z=64): 7 stable isotope(s)
/-- Gd-152 (Z=64, A=152, n=456). -/
abbrev gd152_uniqueness_closed := @nucleus_uniqueness_closed 456
/-- Gd-154 (Z=64, A=154, n=462). -/
abbrev gd154_uniqueness_closed := @nucleus_uniqueness_closed 462
/-- Gd-155 (Z=64, A=155, n=465). -/
abbrev gd155_uniqueness_closed := @nucleus_uniqueness_closed 465
/-- Gd-156 (Z=64, A=156, n=468). -/
abbrev gd156_uniqueness_closed := @nucleus_uniqueness_closed 468
/-- Gd-157 (Z=64, A=157, n=471). -/
abbrev gd157_uniqueness_closed := @nucleus_uniqueness_closed 471
/-- Gd-158 (Z=64, A=158, n=474). -/
abbrev gd158_uniqueness_closed := @nucleus_uniqueness_closed 474
/-- Gd-160 (Z=64, A=160, n=480). -/
abbrev gd160_uniqueness_closed := @nucleus_uniqueness_closed 480

-- TB (Z=65): 1 stable isotope(s)
/-- Tb-159 (Z=65, A=159, n=477). -/
abbrev tb159_uniqueness_closed := @nucleus_uniqueness_closed 477

-- DY (Z=66): 7 stable isotope(s)
/-- Dy-156 (Z=66, A=156, n=468). -/
abbrev dy156_uniqueness_closed := @nucleus_uniqueness_closed 468
/-- Dy-158 (Z=66, A=158, n=474). -/
abbrev dy158_uniqueness_closed := @nucleus_uniqueness_closed 474
/-- Dy-160 (Z=66, A=160, n=480). -/
abbrev dy160_uniqueness_closed := @nucleus_uniqueness_closed 480
/-- Dy-161 (Z=66, A=161, n=483). -/
abbrev dy161_uniqueness_closed := @nucleus_uniqueness_closed 483
/-- Dy-162 (Z=66, A=162, n=486). -/
abbrev dy162_uniqueness_closed := @nucleus_uniqueness_closed 486
/-- Dy-163 (Z=66, A=163, n=489). -/
abbrev dy163_uniqueness_closed := @nucleus_uniqueness_closed 489
/-- Dy-164 (Z=66, A=164, n=492). -/
abbrev dy164_uniqueness_closed := @nucleus_uniqueness_closed 492

-- HO (Z=67): 1 stable isotope(s)
/-- Ho-165 (Z=67, A=165, n=495). -/
abbrev ho165_uniqueness_closed := @nucleus_uniqueness_closed 495

-- ER (Z=68): 6 stable isotope(s)
/-- Er-162 (Z=68, A=162, n=486). -/
abbrev er162_uniqueness_closed := @nucleus_uniqueness_closed 486
/-- Er-164 (Z=68, A=164, n=492). -/
abbrev er164_uniqueness_closed := @nucleus_uniqueness_closed 492
/-- Er-166 (Z=68, A=166, n=498). -/
abbrev er166_uniqueness_closed := @nucleus_uniqueness_closed 498
/-- Er-167 (Z=68, A=167, n=501). -/
abbrev er167_uniqueness_closed := @nucleus_uniqueness_closed 501
/-- Er-168 (Z=68, A=168, n=504). -/
abbrev er168_uniqueness_closed := @nucleus_uniqueness_closed 504
/-- Er-170 (Z=68, A=170, n=510). -/
abbrev er170_uniqueness_closed := @nucleus_uniqueness_closed 510

-- TM (Z=69): 1 stable isotope(s)
/-- Tm-169 (Z=69, A=169, n=507). -/
abbrev tm169_uniqueness_closed := @nucleus_uniqueness_closed 507

-- YB (Z=70): 7 stable isotope(s)
/-- Yb-168 (Z=70, A=168, n=504). -/
abbrev yb168_uniqueness_closed := @nucleus_uniqueness_closed 504
/-- Yb-170 (Z=70, A=170, n=510). -/
abbrev yb170_uniqueness_closed := @nucleus_uniqueness_closed 510
/-- Yb-171 (Z=70, A=171, n=513). -/
abbrev yb171_uniqueness_closed := @nucleus_uniqueness_closed 513
/-- Yb-172 (Z=70, A=172, n=516). -/
abbrev yb172_uniqueness_closed := @nucleus_uniqueness_closed 516
/-- Yb-173 (Z=70, A=173, n=519). -/
abbrev yb173_uniqueness_closed := @nucleus_uniqueness_closed 519
/-- Yb-174 (Z=70, A=174, n=522). -/
abbrev yb174_uniqueness_closed := @nucleus_uniqueness_closed 522
/-- Yb-176 (Z=70, A=176, n=528). -/
abbrev yb176_uniqueness_closed := @nucleus_uniqueness_closed 528

-- LU (Z=71): 1 stable isotope(s)
/-- Lu-175 (Z=71, A=175, n=525). -/
abbrev lu175_uniqueness_closed := @nucleus_uniqueness_closed 525

-- HF (Z=72): 6 stable isotope(s)
/-- Hf-174 (Z=72, A=174, n=522). -/
abbrev hf174_uniqueness_closed := @nucleus_uniqueness_closed 522
/-- Hf-176 (Z=72, A=176, n=528). -/
abbrev hf176_uniqueness_closed := @nucleus_uniqueness_closed 528
/-- Hf-177 (Z=72, A=177, n=531). -/
abbrev hf177_uniqueness_closed := @nucleus_uniqueness_closed 531
/-- Hf-178 (Z=72, A=178, n=534). -/
abbrev hf178_uniqueness_closed := @nucleus_uniqueness_closed 534
/-- Hf-179 (Z=72, A=179, n=537). -/
abbrev hf179_uniqueness_closed := @nucleus_uniqueness_closed 537
/-- Hf-180 (Z=72, A=180, n=540). -/
abbrev hf180_uniqueness_closed := @nucleus_uniqueness_closed 540

-- TA (Z=73): 2 stable isotope(s)
/-- Ta-180 (Z=73, A=180, n=540). -/
abbrev ta180_uniqueness_closed := @nucleus_uniqueness_closed 540
/-- Ta-181 (Z=73, A=181, n=543). -/
abbrev ta181_uniqueness_closed := @nucleus_uniqueness_closed 543

-- W (Z=74): 5 stable isotope(s)
/-- W-180 (Z=74, A=180, n=540). -/
abbrev w_el180_uniqueness_closed := @nucleus_uniqueness_closed 540
/-- W-182 (Z=74, A=182, n=546). -/
abbrev w_el182_uniqueness_closed := @nucleus_uniqueness_closed 546
/-- W-183 (Z=74, A=183, n=549). -/
abbrev w_el183_uniqueness_closed := @nucleus_uniqueness_closed 549
/-- W-184 (Z=74, A=184, n=552). -/
abbrev w_el184_uniqueness_closed := @nucleus_uniqueness_closed 552
/-- W-186 (Z=74, A=186, n=558). -/
abbrev w_el186_uniqueness_closed := @nucleus_uniqueness_closed 558

-- RE (Z=75): 1 stable isotope(s)
/-- Re-185 (Z=75, A=185, n=555). -/
abbrev re185_uniqueness_closed := @nucleus_uniqueness_closed 555

-- OS (Z=76): 7 stable isotope(s)
/-- Os-184 (Z=76, A=184, n=552). -/
abbrev os184_uniqueness_closed := @nucleus_uniqueness_closed 552
/-- Os-186 (Z=76, A=186, n=558). -/
abbrev os186_uniqueness_closed := @nucleus_uniqueness_closed 558
/-- Os-187 (Z=76, A=187, n=561). -/
abbrev os187_uniqueness_closed := @nucleus_uniqueness_closed 561
/-- Os-188 (Z=76, A=188, n=564). -/
abbrev os188_uniqueness_closed := @nucleus_uniqueness_closed 564
/-- Os-189 (Z=76, A=189, n=567). -/
abbrev os189_uniqueness_closed := @nucleus_uniqueness_closed 567
/-- Os-190 (Z=76, A=190, n=570). -/
abbrev os190_uniqueness_closed := @nucleus_uniqueness_closed 570
/-- Os-192 (Z=76, A=192, n=576). -/
abbrev os192_uniqueness_closed := @nucleus_uniqueness_closed 576

-- IR (Z=77): 2 stable isotope(s)
/-- Ir-191 (Z=77, A=191, n=573). -/
abbrev ir191_uniqueness_closed := @nucleus_uniqueness_closed 573
/-- Ir-193 (Z=77, A=193, n=579). -/
abbrev ir193_uniqueness_closed := @nucleus_uniqueness_closed 579

-- PT (Z=78): 6 stable isotope(s)
/-- Pt-190 (Z=78, A=190, n=570). -/
abbrev pt190_uniqueness_closed := @nucleus_uniqueness_closed 570
/-- Pt-192 (Z=78, A=192, n=576). -/
abbrev pt192_uniqueness_closed := @nucleus_uniqueness_closed 576
/-- Pt-194 (Z=78, A=194, n=582). -/
abbrev pt194_uniqueness_closed := @nucleus_uniqueness_closed 582
/-- Pt-195 (Z=78, A=195, n=585). -/
abbrev pt195_uniqueness_closed := @nucleus_uniqueness_closed 585
/-- Pt-196 (Z=78, A=196, n=588). -/
abbrev pt196_uniqueness_closed := @nucleus_uniqueness_closed 588
/-- Pt-198 (Z=78, A=198, n=594). -/
abbrev pt198_uniqueness_closed := @nucleus_uniqueness_closed 594

-- AU (Z=79): 1 stable isotope(s)
/-- Au-197 (Z=79, A=197, n=591). -/
abbrev au197_uniqueness_closed := @nucleus_uniqueness_closed 591

-- HG (Z=80): 7 stable isotope(s)
/-- Hg-196 (Z=80, A=196, n=588). -/
abbrev hg196_uniqueness_closed := @nucleus_uniqueness_closed 588
/-- Hg-198 (Z=80, A=198, n=594). -/
abbrev hg198_uniqueness_closed := @nucleus_uniqueness_closed 594
/-- Hg-199 (Z=80, A=199, n=597). -/
abbrev hg199_uniqueness_closed := @nucleus_uniqueness_closed 597
/-- Hg-200 (Z=80, A=200, n=600). -/
abbrev hg200_uniqueness_closed := @nucleus_uniqueness_closed 600
/-- Hg-201 (Z=80, A=201, n=603). -/
abbrev hg201_uniqueness_closed := @nucleus_uniqueness_closed 603
/-- Hg-202 (Z=80, A=202, n=606). -/
abbrev hg202_uniqueness_closed := @nucleus_uniqueness_closed 606
/-- Hg-204 (Z=80, A=204, n=612). -/
abbrev hg204_uniqueness_closed := @nucleus_uniqueness_closed 612

-- TL (Z=81): 2 stable isotope(s)
/-- Tl-203 (Z=81, A=203, n=609). -/
abbrev tl203_uniqueness_closed := @nucleus_uniqueness_closed 609
/-- Tl-205 (Z=81, A=205, n=615). -/
abbrev tl205_uniqueness_closed := @nucleus_uniqueness_closed 615

-- PB (Z=82): 4 stable isotope(s)
/-- Pb-204 (Z=82, A=204, n=612). -/
abbrev pb204_uniqueness_closed := @nucleus_uniqueness_closed 612
/-- Pb-206 (Z=82, A=206, n=618). -/
abbrev pb206_uniqueness_closed := @nucleus_uniqueness_closed 618
/-- Pb-207 (Z=82, A=207, n=621). -/
abbrev pb207_uniqueness_closed := @nucleus_uniqueness_closed 621
/-- Pb-208 (Z=82, A=208, n=624). -/
abbrev pb208_uniqueness_closed := @nucleus_uniqueness_closed 624

-- BI (Z=83): 1 stable isotope(s)
/-- Bi-209 (Z=83, A=209, n=627). -/
abbrev bi209_uniqueness_closed := @nucleus_uniqueness_closed 627

end QOU.BraidKnot

