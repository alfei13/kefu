package com.kefu.mock.controller;

import com.kefu.mock.model.Coupon;
import com.kefu.mock.repository.CouponRepository;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import java.util.List;

@CrossOrigin
@RestController
@RequestMapping("/api/coupons")
public class CouponController {

    private final CouponRepository couponRepository;

    public CouponController(CouponRepository couponRepository) {
        this.couponRepository = couponRepository;
    }

    @GetMapping
    public List<Coupon> getCouponsByUserId(@RequestParam String userId) {
        return couponRepository.findByUserId(userId);
    }

    @GetMapping("/{code}")
    public Coupon getCouponByCode(@PathVariable String code) {
        return couponRepository.findByCode(code).orElse(null);
    }
}
