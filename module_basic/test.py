{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "cb6fd21b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "숫자 입력> 20\n",
      "125.66368\n",
      "1256.6368\n"
     ]
    }
   ],
   "source": [
    "# main.py 파일\n",
    "import test_module as test\n",
    "\n",
    "radius = test.number_input()\n",
    "print(test.get_circumference(radius))\n",
    "print(test.get_circle_area(radius))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2173bd28",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
