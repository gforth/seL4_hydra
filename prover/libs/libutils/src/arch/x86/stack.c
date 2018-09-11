/*
 * Copyright 2014, NICTA
 *
 * This software may be distributed and modified according to the terms of
 * the BSD 2-Clause license. Note that NO WARRANTY is provided.
 * See "LICENSE_BSD2.txt" for details.
 *
 * @TAG(NICTA_BSD)
 */

#include <autoconf.h>
#include <utils/stack.h>

void *
utils_run_on_stack(void *stack_top, void * (*func)(void *arg), void *arg)
{

#ifdef CONFIG_X86_64
    void *ret;
    asm volatile (
        "movq   %%rsp, %%rcx\n\t"
        "movq   %[new_stack], %%rsp\n\t"
        "push   %%rcx\n\t"
        "movq   %[arg], %%rdi\n\t"
        "call   *%[func]\n\t"
        "add    $0x8, %%rsp\n\t"
        "pop    %%rsp\n\t"
        : [ret] "=a" (ret)
        : [new_stack] "r" (stack_top),
        [func] "r" (func),
        [arg] "r" (arg)
        : "rcx", "rbx", "rdi"
    );
#else
    void *ret;
    asm volatile (
        "mov %%esp, %%ecx\n\t"          /* Save sp. */
        "mov %[new_stack], %%esp\n\t"   /* Switch to new stack. */
        "pushl %%ecx\n\t"               /* Push old sp onto new stack. */
        "pushl %[arg]\n\t"              /* Setup argument to func. */
        "call *%[func]\n\t"
        "add $0x4, %%esp\n\t"
        "popl %%esp\n\t"                /* Switch back! */
        : [ret] "=a" (ret)
        : [new_stack] "r" (stack_top),
        [func] "r" (func),
        [arg] "r" (arg)
        : "ecx", "ebx");
#endif /* CONFIG_X86_64 */
    return ret;
}
