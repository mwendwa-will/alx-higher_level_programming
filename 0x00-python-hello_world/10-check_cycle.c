#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if a cycle exists
 * 
 * @list: takes in a linked list to be checked
 * 
 * @Return: int 
 */

int check_cycle(listint_t *list)
{
    listint_t *new;
    listint_t *runner;

    if (list == NULL)
    {
        return (0);
    }

    new = list;
    runner = list->next;
    while (runner != NULL)
    {
        new = new->next;
        runner = runner->next;
        if (runner != NULL)
        {
            runner = runner->next;
            if (runner == new)
            {
                return (1);
            }
        }
    }
    return (0);
}