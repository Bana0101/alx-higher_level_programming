#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * *insert_node -  inserts a number into a sorted singly linked list
 * @head: the head of the list
 * @number: the number inserted
 * Return: the address of the new node or NULL
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *last, *node;

	current = *head;
	last = *head;
	node = malloc(sizeof(listint_t));
	if (!node)
		return (NULL);
	node->n = number;
	if (!head || !*head)
		return (NULL);
	while (current && current->next)
	{
		if (current->n > number)
		{
			node->next = current;
			last->next = node;
			return (node);
		}
		last = current;
		current = current->next;
	}
	if (current->n > number)
	{
		node->next = current;
		*head = node;
		return (node);
	}
	else
	{
		node = current->next;
		node->next = NULL;
		return (node);
	}
}
