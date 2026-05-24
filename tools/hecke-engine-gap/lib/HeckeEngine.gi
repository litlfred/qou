#############################################################################
##  HeckeEngine.gi — Implementation for the HeckeEngine GAP package.
##
##  Each global function delegates to the corresponding C-extension
##  function defined in src/HeckeEngine.c (kernel-side). The kernel
##  module is loaded via the package's init.g.

InstallGlobalFunction( QOU_HeckeEngine_Version,
function()
    return _QOU_HECKE_C_VERSION();
end );

InstallGlobalFunction( QOU_MarkovZ,
function( q )
    return _QOU_HECKE_C_MARKOV_Z( q );
end );

InstallGlobalFunction( QOU_HeckeH,
function( q )
    return _QOU_HECKE_C_HECKE_H( q );
end );

InstallGlobalFunction( QOU_TraceWeights,
function( q )
    return _QOU_HECKE_C_TRACE_WEIGHTS( q );
end );

InstallGlobalFunction( QOU_GramMatrix,
function( q )
    local flat, M, i, j;
    flat := _QOU_HECKE_C_GRAM_MATRIX_FLAT( q );
    # C ABI returns 36 floats row-major; reshape into a list-of-lists.
    M := NullMat( 6, 6 );
    for i in [1..6] do
        for j in [1..6] do
            M[i][j] := flat[ (i - 1) * 6 + j ];
        od;
    od;
    return M;
end );

InstallGlobalFunction( QOU_GramDet,
function( q )
    return _QOU_HECKE_C_GRAM_DET( q );
end );
