/*
 *  wasm_UI.c
 *
 *  WASM stubs for the SnapPea UI callback functions.
 *  Replaces unix_UI.c for the WebAssembly build.
 */

#include "SnapPea.h"
#include <stdio.h>
#include <stdlib.h>

#include "kernel_namespace.h"

void uAcknowledge(
    const char *message)
{
    /* No-op in WASM — caller can check error returns instead */
    (void)message;
}

void uFatalError(
    const char    *function,
    const char    *file)
{
    /*
     *  In WASM we can't call exit() cleanly. Instead we abort,
     *  which Emscripten will turn into a JS exception.
     */
    fprintf(
        stderr,
        "SnapPea fatal error in %s() in %s.c\n",
        function,
        file);
    abort();
}

void uAbortMemoryFull(void)
{
    fprintf(stderr, "SnapPea: out of memory\n");
    abort();
}

int uQuery(
    const char  *message,
    const int   num_responses,
    const char  *responses[],
    const int   default_response)
{
    /* Always return the default — no interactive UI in WASM */
    (void)message;
    (void)num_responses;
    (void)responses;
    return default_response;
}

/*
 *  Long computation callbacks.
 *  These are no-ops for now. A future version could allow JS
 *  callback registration for cancellation support.
 */
Boolean gLongComputationInProgress,
        gLongComputationCancelled;

void uLongComputationBegins(
    const char    *message,
    Boolean is_abortable)
{
    (void)message;
    (void)is_abortable;
}

FuncResult uLongComputationContinues(void)
{
    return func_OK;
}

void uLongComputationEnds(void)
{
}

#include "end_namespace.h"
