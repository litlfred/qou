#!/usr/bin/env python3
"""
Generate the appendix markdown table: all 92 elements in (p,n) notation.
Outputs markdown suitable for insertion into the content block .md file.
"""

import math
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "folio-assistant"))
from computations.q_parameter import Q

q = Q
hbar_q = 1.0 - 1.0 / q
q_half = math.sqrt(q)

mu_u, mu_d = 311.10, 312.39

def S(a, b):
    return (q * a + (1/q) * b) / (q_half + 1/q_half)

m_p = S(mu_u, mu_u) + 2 * S(mu_u, mu_d)
m_n = 2 * S(mu_u, mu_d) + S(mu_d, mu_d)
m_e = 0.51099895

elements = [
    ( 1,   1, "H",   "Hydrogen",      0.0000),
    ( 2,   4, "He",  "Helium",        7.0739),
    ( 3,   7, "Li",  "Lithium",       5.6063),
    ( 4,   9, "Be",  "Beryllium",     6.4628),
    ( 5,  11, "B",   "Boron",         6.9277),
    ( 6,  12, "C",   "Carbon",        7.6801),
    ( 7,  14, "N",   "Nitrogen",      7.4756),
    ( 8,  16, "O",   "Oxygen",        7.9762),
    ( 9,  19, "F",   "Fluorine",      7.7790),
    (10,  20, "Ne",  "Neon",          8.0325),
    (11,  23, "Na",  "Sodium",        8.1115),
    (12,  24, "Mg",  "Magnesium",     8.2607),
    (13,  27, "Al",  "Aluminium",     8.3316),
    (14,  28, "Si",  "Silicon",       8.4477),
    (15,  31, "P",   "Phosphorus",    8.4812),
    (16,  32, "S",   "Sulfur",        8.4932),
    (17,  35, "Cl",  "Chlorine",      8.5203),
    (18,  40, "Ar",  "Argon",         8.5954),
    (19,  39, "K",   "Potassium",     8.5570),
    (20,  40, "Ca",  "Calcium",       8.5513),
    (21,  45, "Sc",  "Scandium",      8.6190),
    (22,  48, "Ti",  "Titanium",      8.7230),
    (23,  51, "V",   "Vanadium",      8.7420),
    (24,  52, "Cr",  "Chromium",      8.7760),
    (25,  55, "Mn",  "Manganese",     8.7649),
    (26,  56, "Fe",  "Iron",          8.7903),
    (27,  59, "Co",  "Cobalt",        8.7680),
    (28,  58, "Ni",  "Nickel",        8.7322),
    (29,  63, "Cu",  "Copper",        8.7522),
    (30,  64, "Zn",  "Zinc",          8.7357),
    (31,  69, "Ga",  "Gallium",       8.7246),
    (32,  74, "Ge",  "Germanium",     8.7264),
    (33,  75, "As",  "Arsenic",       8.7010),
    (34,  80, "Se",  "Selenium",      8.7110),
    (35,  79, "Br",  "Bromine",       8.6961),
    (36,  84, "Kr",  "Krypton",       8.7172),
    (37,  85, "Rb",  "Rubidium",      8.6974),
    (38,  88, "Sr",  "Strontium",     8.7326),
    (39,  89, "Y",   "Yttrium",       8.7138),
    (40,  90, "Zr",  "Zirconium",     8.7098),
    (41,  93, "Nb",  "Niobium",       8.6641),
    (42,  98, "Mo",  "Molybdenum",    8.6353),
    (43,  98, "Tc",  "Technetium",    8.5937),
    (44, 102, "Ru",  "Ruthenium",     8.6070),
    (45, 103, "Rh",  "Rhodium",       8.5843),
    (46, 106, "Pd",  "Palladium",     8.5670),
    (47, 107, "Ag",  "Silver",        8.5536),
    (48, 114, "Cd",  "Cadmium",       8.5398),
    (49, 115, "In",  "Indium",        8.5160),
    (50, 120, "Sn",  "Tin",           8.5050),
    (51, 121, "Sb",  "Antimony",      8.4820),
    (52, 130, "Te",  "Tellurium",     8.4390),
    (53, 127, "I",   "Iodine",        8.4455),
    (54, 132, "Xe",  "Xenon",         8.4275),
    (55, 133, "Cs",  "Caesium",       8.4100),
    (56, 138, "Ba",  "Barium",        8.3937),
    (57, 139, "La",  "Lanthanum",     8.3780),
    (58, 140, "Ce",  "Cerium",        8.3765),
    (59, 141, "Pr",  "Praseodymium",  8.3540),
    (60, 142, "Nd",  "Neodymium",     8.3460),
    (61, 145, "Pm",  "Promethium",    8.3040),
    (62, 152, "Sm",  "Samarium",      8.2440),
    (63, 153, "Eu",  "Europium",      8.2290),
    (64, 158, "Gd",  "Gadolinium",    8.2140),
    (65, 159, "Tb",  "Terbium",       8.1990),
    (66, 164, "Dy",  "Dysprosium",    8.1865),
    (67, 165, "Ho",  "Holmium",       8.1710),
    (68, 166, "Er",  "Erbium",        8.1690),
    (69, 169, "Tm",  "Thulium",       8.1460),
    (70, 174, "Yb",  "Ytterbium",     8.1280),
    (71, 175, "Lu",  "Lutetium",      8.1165),
    (72, 180, "Hf",  "Hafnium",       8.0985),
    (73, 181, "Ta",  "Tantalum",      8.0870),
    (74, 184, "W",   "Tungsten",      8.0639),
    (75, 187, "Re",  "Rhenium",       8.0390),
    (76, 192, "Os",  "Osmium",        8.0194),
    (77, 193, "Ir",  "Iridium",       8.0060),
    (78, 195, "Pt",  "Platinum",      7.9930),
    (79, 197, "Au",  "Gold",          7.9759),
    (80, 202, "Hg",  "Mercury",       7.9530),
    (81, 205, "Tl",  "Thallium",      7.9370),
    (82, 208, "Pb",  "Lead",          7.8675),
    (83, 209, "Bi",  "Bismuth",       7.8480),
    (84, 209, "Po",  "Polonium",      7.8352),
    (85, 210, "At",  "Astatine",      7.8147),
    (86, 222, "Rn",  "Radon",         7.7227),
    (87, 223, "Fr",  "Francium",      7.7095),
    (88, 226, "Ra",  "Radium",        7.6620),
    (89, 227, "Ac",  "Actinium",      7.6510),
    (90, 232, "Th",  "Thorium",       7.6150),
    (91, 231, "Pa",  "Protactinium",  7.6138),
    (92, 238, "U",   "Uranium",       7.5701),
]

magic_Z = {2, 8, 20, 28, 50, 82}
magic_N = {2, 8, 20, 28, 50, 82, 126}

# Print markdown table
print("| $\\#$ | Element | $p$ | $n$ | Knot formula | $\\mathcal{M}_{\\mathrm{QOU}}$ (MeV) | $B/A$ (MeV) |")
print("|---:|---------|---:|---:|-------------|---:|---:|")

for Z, A, sym, name, B_A in elements:
    N = A - Z
    B_total = A * B_A
    m_qou = Z * m_p + N * m_n - B_total + Z * m_e

    formula = f"${Z}\\mathfrak{{p}} \\bowtie {N}\\mathfrak{{n}} \\bowtie {Z}T_{{2,3}}$"

    markers = ""
    if Z in magic_Z:
        markers += "$^{\\diamond}$"
    if N in magic_N:
        markers += "$^{\\star}$"

    print(f"| {Z} | {name}{markers} | {Z} | {N} | {formula} | ${m_qou:.1f}$ | ${B_A:.4f}$ |")
