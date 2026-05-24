/*
 * HeckeEngine.c — GAP C-extension wrapping hecke-engine-c.
 *
 * Each function is registered with GAP's kernel as `_QOU_HECKE_C_X`
 * (matching the InstallGlobalFunction wiring in lib/HeckeEngine.gi).
 * Each delegates to the corresponding `qou_hecke_*` function exported
 * by libhecke_engine_c.{so,dylib} (built from tools/hecke-engine-c/).
 *
 * Build:
 *   cd src && ./configure --with-gaproot=<gap-installation-root> && make
 *
 * The configure script (provided by GAP's package template, not in
 * this scaffold) writes the Makefile that links against both GAP's
 * kernel and libhecke_engine_c.
 */

#include "gap_all.h"
#include "hecke_engine.h"    /* from tools/hecke-engine-c/include/ */

/* ── version ── */
static Obj QouHeckeCVersion(Obj self) {
    const char* v = qou_hecke_version();
    return MakeString(v);
}

/* ── scalar f64 → f64 helpers ── */
static Obj QouHeckeCMarkovZ(Obj self, Obj q) {
    if (!IS_FLOAT(q)) ErrorMayQuit("QOU_MarkovZ: q must be a float", 0, 0);
    return NEW_MACFLOAT(qou_hecke_markov_z(VAL_MACFLOAT(q)));
}

static Obj QouHeckeCHeckeH(Obj self, Obj q) {
    if (!IS_FLOAT(q)) ErrorMayQuit("QOU_HeckeH: q must be a float", 0, 0);
    return NEW_MACFLOAT(qou_hecke_h(VAL_MACFLOAT(q)));
}

static Obj QouHeckeCGramDet(Obj self, Obj q) {
    if (!IS_FLOAT(q)) ErrorMayQuit("QOU_GramDet: q must be a float", 0, 0);
    return NEW_MACFLOAT(qou_hecke_gram_det(VAL_MACFLOAT(q)));
}

/* ── vector returns (length-6 floats) ── */
static Obj QouHeckeCTraceWeights(Obj self, Obj q) {
    if (!IS_FLOAT(q)) ErrorMayQuit("QOU_TraceWeights: q must be a float", 0, 0);
    double out[6];
    qou_hecke_trace_weights(VAL_MACFLOAT(q), out);

    Obj list = NEW_PLIST(T_PLIST_DENSE_NHOM, 6);
    SET_LEN_PLIST(list, 6);
    for (int i = 0; i < 6; i++) {
        SET_ELM_PLIST(list, i + 1, NEW_MACFLOAT(out[i]));
        CHANGED_BAG(list);
    }
    return list;
}

/* ── 36-float gram-matrix flatten ── */
static Obj QouHeckeCGramMatrixFlat(Obj self, Obj q) {
    if (!IS_FLOAT(q)) ErrorMayQuit("QOU_GramMatrix: q must be a float", 0, 0);
    double out[36];
    qou_hecke_gram_matrix_flat(VAL_MACFLOAT(q), out);

    Obj list = NEW_PLIST(T_PLIST_DENSE_NHOM, 36);
    SET_LEN_PLIST(list, 36);
    for (int i = 0; i < 36; i++) {
        SET_ELM_PLIST(list, i + 1, NEW_MACFLOAT(out[i]));
        CHANGED_BAG(list);
    }
    return list;
}

/* ── GAP registration table ── */
static StructGVarFunc GVarFuncs[] = {
    GVAR_FUNC(_QOU_HECKE_C_VERSION,         0, ""),
    GVAR_FUNC(_QOU_HECKE_C_MARKOV_Z,        1, "q"),
    GVAR_FUNC(_QOU_HECKE_C_HECKE_H,         1, "q"),
    GVAR_FUNC(_QOU_HECKE_C_TRACE_WEIGHTS,   1, "q"),
    GVAR_FUNC(_QOU_HECKE_C_GRAM_MATRIX_FLAT,1, "q"),
    GVAR_FUNC(_QOU_HECKE_C_GRAM_DET,        1, "q"),
    { 0, 0, 0, 0, 0 }
};

static Int InitKernel(StructInitInfo* module) {
    InitHdlrFuncsFromTable(GVarFuncs);
    return 0;
}

static Int InitLibrary(StructInitInfo* module) {
    InitGVarFuncsFromTable(GVarFuncs);
    return 0;
}

static StructInitInfo module = {
    /* type        = */ MODULE_DYNAMIC,
    /* name        = */ "HeckeEngine",
    /* revision_c  = */ 0,
    /* revision_h  = */ 0,
    /* version     = */ 0,
    /* crc         = */ 0,
    /* initKernel  = */ InitKernel,
    /* initLibrary = */ InitLibrary,
    /* checkInit   = */ 0,
    /* preSave     = */ 0,
    /* postSave    = */ 0,
    /* postRestore = */ 0,
};

StructInitInfo* Init__Dynamic(void) {
    return &module;
}
