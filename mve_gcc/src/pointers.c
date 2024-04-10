#include <stdio.h>
#include <string.h>

// Takes an integer parameter
int simple_int_function(int param) {
    printf("[AA]: Value of param is %d\n", param);
    return param;
}

/**
 * A pointer review for the devs who can't QUITE remember the
 * tricks.
 *
 * For more details, I recommend reading "Everything you need to know
 * about pointers in C" by Peter Hosey. Found here:
 * 	http://boredzo.org/pointers/
 *
 * This demo borrows a lot of their code, but is provided here as a
 * ready-to-run tutorial. It also has a lot of experiments as "proofs"
 * of how these things work.
 * */

int main(void) {

	/* ****************** *
	 * Basic Pointers
	 * ****************** */
	printf("\nBasic Pointers\n\n");

	// Declare a variable; it occupies some memory
	int var = 23;
	printf("[1] %d\n", var);

	// & is the "address-of-operator"
	// Create an int pointer that points to var
	int *var_ptr = &var;

	// The VALUE of the ptr is the ADDRESS of var ...
	printf("[2] %p == %p\n", &var, var_ptr);

	// ... and has it's own unique ADDRESS
	printf("[3] %p\n", &var_ptr);

	// The * operator dereferences (GETS) the value in the address!
	printf("[4] %d\n", *var_ptr);

	// If we change var, we expect the value of var_ptr to change as well
	var = 55;
	printf("[5] %d == %d\n", var, *var_ptr);

	// If we change var_ptr, we expect the value of var to change as well
	*var_ptr = 22;
	printf("[6] %d == %d\n", *var_ptr, var);

	// NOTE: assigning a value directly to the pointer will cause a crash!
	// This changes the ADDRESS of the pointer, not the value!
	// Uncomment the block below and notice the failure.
	 /* var_ptr = 8;
	 printf("%d == %d\n", var, *var_ptr);
	 printf("We won't print this line with the above 2 lines un-commented"); */


	/* ****************** *
	 * Arrays
	 * ****************** */
	printf("\nArray Logic\n\n");

	// This array has three 'ints' worth of space
	int array[] = { 45, 67, 89 };

	// Thanks to decay, using the `array` name itself POINTS to the address
	// of the first element. This means array expressions work a lot like
	// pointers!
	printf("[7] %p == %p\n", array, &array[0]);

	// dereferencing the array is the same as getting the first value explicitly
	printf("[8] %d == %d\n", *array, array[0]);

	// However, array arithmetic doesn't work like pointer arithmetic
	// (increment pointer after accessing).
	// attempting *(array++) will crash
	int *array_ptr = array;
	printf("[9]  first element: %d\n", *(array_ptr++));
	printf("[10] second element: %d\n", *(array_ptr++));
	printf("[11] third element: %d\n", *array_ptr);

	// Note: due to decay, you can point a var at any "index" of the arrray
	// Doing the following loses the references to the FIRST 'array' value
	int *array_ptr_two = &array[1];
	printf("[12] %d\n", array_ptr_two[0]);
	printf("[13] %d\n", array_ptr_two[1]);


	/* ****************** *
	 * Structs & Unions
	 * ****************** */
	printf("\nStruct & Union Logic\n\n");

	struct mystruct {
		int answer;
	};

	// Basic access of a member
	struct mystruct data;
	data.answer = 42;

	printf("[14]: %d\n", data.answer);

	// How many ways can we access and assign struct members?
	struct mystruct *struct_ptr = &data;

	// 01: Standard "address-of" and * operators
	// print the ADDRESS and VALUE of the member
	printf("[15]: %p\n", &(*struct_ptr).answer);
	printf("[16]: %d\n", (*struct_ptr).answer);

	// update
	(*struct_ptr).answer = 01;
	printf("[17]: %d\n", (*struct_ptr).answer);

	// 02: "pointer-to-member" operator
	struct_ptr->answer = 22;
	printf("[18]: %d\n", struct_ptr->answer);

	// 03: Multiple indirection

	// Let us create a pointer who points to another pointer
	struct mystruct **struct_ptr_ptr = &struct_ptr;

	// I can access the value stored in the pointer's pointer directly...
	printf("[20]: %d\n", (**struct_ptr_ptr).answer);

	// ... or by the (pointer to pointer)-to-member operator
	printf("[21]: %d\n", (*struct_ptr_ptr)->answer);

	printf("\n");

	// What if we have decaying arrays in our struct?
	struct myemail {
		char message[3];
	} email = {
			{"HI!"}
	};

	// Recall you print a single member vs entire char array using the formatter
	printf("[22]: %c vs %s\n", email.message[0], email.message);

	// You can also print from the middle of an array with the address operator
	printf("[23]: %s\n", &email.message[1]);

	// Create a pointer to the struct; How to access the values now?
	struct myemail *email_ptr = &email;

	// Exactly the same as before!
	printf("[24]: %c vs %c vs %s\n", (*email_ptr).message[0], email_ptr->message[1], email_ptr->message);


	/* ****************** *
	 * Function Pointers
	 * ****************** */
	printf("\nFunction Pointers\n\n");

	// Like vars, functions have addresses too! You can point a matching
	// signature to an existing address
	int (*func_ptr)(int);
	func_ptr = &simple_int_function;

	// You can invoke this function with pointer
	simple_int_function(11);
	(*func_ptr)(22);

	printf("\n");

	return 0;
}
