{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "6632d8e5-31be-47e9-9d62-e4e950ad5aa0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['hello,', ' ', 'world.', ' ', 'this,', ' ', 'is', ' ', 'a', ' ', 'test.']\n"
     ]
    }
   ],
   "source": [
    "import re\n",
    "text=\"hello, world. this, is a test.\"\n",
    "result=re.split(r'(\\s)',text)\n",
    "print(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "ae4cd675-0914-450d-96e1-1d6e8c6ac542",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['hello,', ' ', 'world.', ' ', 'this,', ' ', 'is', ' ', 'a', ' ', 'test.']\n"
     ]
    }
   ],
   "source": [
    "tesult=re.split(r'([,.]|\\s)',text)\n",
    "print(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "6ab01cb4-16bb-4886-8996-5a26554cb56b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['hello,', 'world.', 'this,', 'is', 'a', 'test.']\n"
     ]
    }
   ],
   "source": [
    "result=[item for item in result if item.strip()]\n",
    "print(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "248833cb-c35f-43ea-abdd-4e7efda439cd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['लवली', 'प्रोफेशनल', 'यूनिवर्सिटी', '(', 'LPU', ')', 'भारत', 'की', 'एक', 'प्रमुख', 'निजी', 'विश्वविद्यालय', 'है', 'जो', 'पंजाब', 'के', 'जगाधरी-फगवाड़ा', 'रोड', ',', 'फगवाड़ा', 'में', 'स्थित', 'है।', 'यह', 'विश्वविद्यालय', 'विविध', 'पाठ्यक्रमों', 'में', 'उच्च', 'गुणवत्ता', 'वाली', 'शिक्षा', 'प्रदान', 'करता', 'है', ',', 'जैसे', 'इंजीनियरिंग', ',', 'प्रबंधन', ',', 'कानून', ',', 'चिकित्सा', ',', 'कला', ',', 'डिजाइन', 'और', 'कंप्यूटर', 'विज्ञान।', 'LPU', 'का', 'उद्देश्य', 'छात्रों', 'को', 'व्यावहारिक', 'ज्ञान', ',', 'नवीन', 'तकनीकों', 'और', 'वैश्विक', 'कौशलों', 'से', 'लैस', 'करना', 'है', 'ताकि', 'वे', 'भविष्य', 'की', 'चुनौतियों', 'का', 'सामना', 'आत्म-विश्वास', 'के', 'साथ', 'कर', 'सकें।', 'यहाँ', 'का', 'शैक्षणिक', 'माहौल', 'आधुनिक', 'सुविधाओं', ',', 'अनुभवी', 'शिक्षकों', 'और', 'उद्योग-अनुप्रयुक्त', 'कार्यक्रमों', 'के', 'कारण', 'छात्रों', 'के', 'सर्वांगीण', 'विकास', 'में', 'सहायक', 'होता', 'है।', 'LPU', 'में', 'राष्ट्रीय', 'और', 'अंतर्राष्ट्रीय', 'स्तर', 'पर', 'पहचान', 'प्राप्त', 'करने', 'के', 'लिए', 'शोध', ',', 'इंटर्नशिप', 'और', 'सांस्कृतिक', 'गतिविधियों', 'पर', 'भी', 'विशेष', 'ध्यान', 'दिया', 'जाता', 'है।']\n",
      "727\n",
      "115\n",
      "1\n"
     ]
    }
   ],
   "source": [
    "import re\n",
    "\n",
    "text = \"लवली प्रोफेशनल यूनिवर्सिटी (LPU) भारत की एक प्रमुख निजी विश्वविद्यालय है जो पंजाब के जगाधरी-फगवाड़ा रोड, फगवाड़ा में स्थित है। यह विश्वविद्यालय विविध पाठ्यक्रमों में उच्च गुणवत्ता वाली शिक्षा प्रदान करता है, जैसे इंजीनियरिंग, प्रबंधन, कानून, चिकित्सा, कला, डिजाइन और कंप्यूटर विज्ञान। LPU का उद्देश्य छात्रों को व्यावहारिक ज्ञान, नवीन तकनीकों और वैश्विक कौशलों से लैस करना है ताकि वे भविष्य की चुनौतियों का सामना आत्म-विश्वास के साथ कर सकें। यहाँ का शैक्षणिक माहौल आधुनिक सुविधाओं, अनुभवी शिक्षकों और उद्योग-अनुप्रयुक्त कार्यक्रमों के कारण छात्रों के सर्वांगीण विकास में सहायक होता है। LPU में राष्ट्रीय और अंतर्राष्ट्रीय स्तर पर पहचान प्राप्त करने के लिए शोध, इंटर्नशिप और सांस्कृतिक गतिविधियों पर भी विशेष ध्यान दिया जाता है।\"\n",
    "\n",
    "result = re.split(r'(--|[,.:;?_!\"()\\']|\\s)', text)\n",
    "result = [item.strip() for item in result if item.strip()]\n",
    "\n",
    "print(result)\n",
    "print(len(text))\n",
    "words = text.split()\n",
    "count = len(words)\n",
    "\n",
    "print(count)\n",
    "\n",
    "sentences = re.split(r'[.!?]+', text)\n",
    "sentences = [s.strip() for s in sentences if s.strip()]\n",
    "\n",
    "print(len(sentences))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "67a83299-efab-4e46-8eea-f7f77c5d33cc",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python (Anaconda)",
   "language": "python",
   "name": "anaconda"
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
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
