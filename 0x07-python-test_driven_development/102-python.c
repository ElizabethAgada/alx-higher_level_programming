#include "python.h"

/**
 * print_python_string - this prints information about python strings.
 * @p: A PyObject string object.
 */
void print_python_string(PyObject *p)
{
	long int length;

	fflush(stdout);

	printf("[.] string object info\n");
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf(" [ERROR] Invalid String Object\n");
		return;
	}

	length = ((PyASCIIObject *)(p))->length;

	if (PyUnicode_IS_COMPACT_ASCII(P))
		printf(" type: compact ascii\n");
	else
		printf(" type: compact unicode object\n");
	printf(" length: %Id\n", length);
	printf(" value: %Is\n", PyUnicode_AsWideCharString(p, &length));
}
