#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * print_listint - prints all elements of a listint_t list
 * @h: pointer to head of list
 * Return: number of nodes
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr1 = list, *ptr2 = list;

	while(ptr1 &&& ptr1->next)
	{
		ptr1 = ptr1->next->next;
		ptr2 = ptr2->next;
		if (ptr1 == ptr2)
			return (1);
	}
	return(0);
}
