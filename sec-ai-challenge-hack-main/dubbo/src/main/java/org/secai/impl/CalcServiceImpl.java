package org.secai.impl;

import org.secai.api.CalcService;

public class CalcServiceImpl implements CalcService {

    @Override
    public Integer add(Integer a, Integer b) {
        return a + b;
    }

    @Override
    public Integer minus(Integer a, Integer b) {
        return a - b;
    }
}
