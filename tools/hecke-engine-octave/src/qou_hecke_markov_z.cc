// qou_hecke_markov_z.cc — z = q^3 / (q^2 + 1), trace convention D
// (SU(2)/Temperley-Lieb). Convention C excised 2026-08-09.
#include "mex.h"
#include "hecke_engine.h"

void mexFunction(int nlhs, mxArray *plhs[],
                 int nrhs, const mxArray *prhs[]) {
    if (nrhs != 1) mexErrMsgTxt("Usage: z = qou_hecke_markov_z(q)");
    if (nlhs > 1) mexErrMsgTxt("Too many output arguments.");
    if (!mxIsDouble(prhs[0]) || mxGetNumberOfElements(prhs[0]) != 1)
        mexErrMsgTxt("q must be a scalar double.");
    double q = mxGetScalar(prhs[0]);
    plhs[0] = mxCreateDoubleScalar(qou_hecke_markov_z(q));
}
