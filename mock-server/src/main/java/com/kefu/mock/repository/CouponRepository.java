package com.kefu.mock.repository;

import com.kefu.mock.model.Coupon;
import org.springframework.data.jpa.repository.JpaRepository;
import java.util.List;
import java.util.Optional;

public interface CouponRepository extends JpaRepository<Coupon, Long> {
    List<Coupon> findByUserId(String userId);
    Optional<Coupon> findByCode(String code);
}
