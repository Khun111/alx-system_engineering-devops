#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int infinite_while(void);

/**
 * main - create zombie
 * Return: 0 on success
 */
int main(void)
{
	int i;
	pid_t zombie;

	for (i = 0; i < 5; i++)
	{
		zombie = fork();
		if (zombie == 0)
		{
			printf(" Zombie process created, PID: %d\n", getpid());
			exit(0);
		}
	}
	infinite_while();
	return (0);
}

/**
 * infinite_while - infinite loop
 * Return: 0 on success
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

