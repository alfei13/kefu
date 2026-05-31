package com.kefu.mock.repository;

import com.kefu.mock.model.AfterSaleRequest;
import org.springframework.data.jpa.repository.JpaRepository;
import java.util.List;

public interface AfterSaleRepository extends JpaRepository<AfterSaleRequest, Long> {
    List<AfterSaleRequest> findByOrderId(Long orderId);
}
